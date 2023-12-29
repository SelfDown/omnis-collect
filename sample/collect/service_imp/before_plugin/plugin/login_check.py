# -*- coding: utf-8 -*-
from collect.utils.collect_utils import get_safe_data, get_key

from collect.service_imp.before_plugin.before_plugin import BeforePlugin


class LoginCheck(BeforePlugin):
    LCConst = {
        "must_login_name": "must_login",
        "must_token_name": "must_token",
        "token_name": "token",
        "check_ip_name": "check_ip"
    }

    def get_token_name(self):
        return self.LCConst["token_name"]

    def get_must_login_name(self):
        return self.LCConst["must_login_name"]

    def get_must_token_name(self):
        return self.LCConst["must_token_name"]
    def get_check_ip_name(self):
        return self.LCConst["check_ip_name"]

    # must_login = True
    # if self.get_must_login_name() in self.template:
    #     must_login = self.template[self.get_must_login_name()]
    # if must_login and self.op_user == '-1':
    #     self.log(self.get_template_service_name())
    #     return self.fail(msg="请重新登录")
    # else:
    #     return self.success(data=[])
    def handler(self, params, template):
        must_login_name = self.get_must_login_name()
        if must_login_name not in template:
            must_login = True
        else:
            must_login = template[must_login_name]
        must_token = get_safe_data(self.get_must_token_name(), template, False)

        # must_token 的权限大于must_login,如果有token ,就不必登录了
        no_auth_service = get_key("no_auth_service","")
        header = self.get_header(template)
        if must_token:
            token = header.get("HTTP_" + self.get_token_name().upper())
            config_token = get_key(self.get_token_name())
            if token != config_token:
                return self.fail("接入的token 不正确")
        elif must_login == True and self.op_user == '-1' and self.get_current_service(template) not in no_auth_service:
            return self.fail("请重新登录")

        def get_ip():
            x_forwarded_for = header.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
            else:
                ip = header.get('REMOTE_ADDR')  # 这里获得代理ip
            return ip

        check_ip = get_safe_data(self.get_check_ip_name(), template, False)
        # 登录IP 验证
        if check_ip:
            current_ip = get_ip()
            allow_ip = get_key("allow_ip","")
            if current_ip not in allow_ip.split(","):
                return self.fail("当前IP 禁止访问")

        return self.success(params)
