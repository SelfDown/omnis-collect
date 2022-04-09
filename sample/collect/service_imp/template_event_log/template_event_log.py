# -*- coding: utf-8 -*-
import threading

from collect.utils.collect_utils import Singleton, get_safe_data, get_key


@Singleton
class TemplateEventLog:
    def __init__(self):
        from collect.utils.log import get_collect_log
        self.logger = get_collect_log()
        self.log("模板事件初始化")
        import Queue
        self.q = Queue.Queue()
        t1 = threading.Thread(target=self.handler_log_data, )
        t1.start()

    def handler_log_data(self):
        """
        处理消息队列
        """
        q = self.q
        while True:
            import time
            while not q.empty():
                time.sleep(3)
                qsize = q.qsize()
                self.log("获取到消息：" + str(qsize))
                if qsize > 10000:
                    qsize = 10000

                data_list = []
                for item in xrange(qsize):
                    data = q.get()
                    data_list.append(data)
                if len(data_list) > 0:
                    from collect.service.template_service import TemplateService
                    t = TemplateService(op_user="sys")
                    save_service = get_key("log_handler_service")
                    if not save_service:
                        continue
                    service = {
                        "service": save_service,
                        "data_list": data_list
                    }
                    try:
                        result = t.result(service, is_http=False)
                        if not t.is_success(result):
                            self.log(t.get_msg(result), "error")
                    except Exception as e:
                        self.log("系统运行错误:" + str(e))
                        pass
            time.sleep(5)

    def log(self, msg, level=None):
        if not level:
            self.logger.info(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "warn":
            self.logger.warn(msg)

    def add_template_event(self, log_type, data):
        """
        添加模板事件
        """
        item = {
            "type": log_type,
            "data": data
        }
        self.q.put(item)
