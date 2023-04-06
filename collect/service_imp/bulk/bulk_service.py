# -*- coding: utf-8 -*-
"""
@Time: 2021/8/19 17:57
@Author: zzhang zzhang@cenboomh.com
@File: bulk_service.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data
import threading


class BulkThread(threading.Thread):
    def __init__(self, func, args=()):
        super(BulkThread, self).__init__()
        self.func = func
        self.args = args
        self.result = {}

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result, None  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception as e:
            return {}, str(e)


class BulkThreadList():
    """
     获取线程运行同一个方法
    """

    def __init__(self, func, max_once=30):
        """

        :param func:  运行方法
        :param max_once:  单次运行个数
        """
        self.func = func
        self.args_list = []
        self.li = []
        self.max_once = max_once

    def add_data(self, args=()):

        th = BulkThread(func=self.func, args=args)
        self.li.append(th)

    def get_results(self):
        """
        防止钉钉请求数过大，将请求成{max_once}个一组
        :return:
        """
        results = []
        start = 0
        err_msg_list = []
        for th_item in range(0, len(self.li), self.max_once):
            uli = self.li[start:th_item + self.max_once]
            start = th_item + self.max_once
            for item in uli:
                item.start()
            for item in uli:
                item.join()
                result, err_msg = item.get_result()
                if not err_msg:
                    results.append(result)
                else:
                    err_msg_list.append(err_msg)

        self.li = []
        return results, err_msg_list


class ServiceBulkService(CollectService):
    bs_const = {
        "batch_name": "batch",
        "item_name": "item",
        "max_once_name": "max_once",
        "append_param_name": "append_param",
        "append_item_param_name": "append_item_param",
    }

    def get_item_name(self):
        return self.bs_const["item_name"]

    def get_append_param_name(self):
        return self.bs_const["append_param_name"]

    def get_append_item_param_name(self):
        return self.bs_const["append_item_param_name"]

    def get_max_once_name(self):
        return self.bs_const["max_once_name"]

    def get_batch_name(self):
        return self.bs_const["batch_name"]

    def get_batch(self):
        return get_safe_data(self.get_batch_name(), self.template)

    def __init__(self, op_user):
        CollectService.__init__(self, op_user=op_user)

    def get_node_result(self, node, params, template):
        from django.http import QueryDict
        if isinstance(params, QueryDict):
            params = params.dict()
        append_param = True

        if self.get_append_param_name() in node:
            append_param = node[self.get_append_param_name()]

        append_item = get_safe_data(self.get_append_item_param_name(), node, False)
        if append_item:
            append_param = True
            item = get_safe_data(self.get_item_name(), params)
            if not isinstance(item, dict):
                item = {self.get_item_name():item}
            params = dict(params.items() + item.items())
        service_data = self.get_node_service(node=node, params=params, template=template,
                                             append_param=append_param)
        if not service_data:
            return service_data
        service = self.get_data(service_data)
        service_result = self.get_service_result(service, self.template)
        return service_result

    def result(self, params):
        params_result = self.get_params_result()
        batch = self.get_batch()
        if not batch:
            return self.fail("配置中没有找到【" + self.get_batch_name() + "】标签")

        foreach_name = get_safe_data(self.get_foreach_name(), batch)
        if not foreach_name:
            return self.fail("配置中没有找到【" + self.get_foreach_name() + "】标签")
        max_once = get_safe_data(self.get_max_once_name(), batch, 30)
        foreach = get_safe_data(foreach_name, params_result)
        if not foreach:
            # return self.fail("参数中没有找到【" + foreach_name + "】变量")
            return self.success([])
        item_name = get_safe_data(self.get_item_name(), batch)
        if not item_name:
            return self.fail("配置中没有找到【" + self.get_item_name() + "】标签")

        result_list = []
        btl = BulkThreadList(func=self.get_node_result, max_once=max_once)
        if len(foreach) > 1000:
            return self.fail("服务不能超过1000个")
        if self.can_log():
            self.log("总共运行" + str(len(foreach)) + "服务")
        reqList = []
        for index, item in enumerate(foreach):
            import copy
            batch_tmp = copy.deepcopy(batch)
            params_tmp = copy.deepcopy(params_result)
            if self.can_log():
                self.log(self.get_template_service_name() + "添加第 " + str(index + 1) + " 个服务")
            params_tmp[item_name] = item
            reqList.append(item)
            btl.add_data(args=(batch_tmp, params_tmp, self.template))
        results, err_msg_list = btl.get_results()
        if err_msg_list:
            self.log("批量执行报错")
            self.log(err_msg_list)
        for service_result, req in zip(results, reqList):
            service_result[self.get_item_name()] = req
            result_list.append(service_result)
        save_field = get_safe_data(self.get_save_field_name(), batch)
        if save_field:
            params_result[save_field] = result_list
        return self.success({})
