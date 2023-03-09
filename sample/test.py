# -*- coding: utf-8 -*-
from collect.service.template_service import TemplateService

template = TemplateService(op_user="sys")
pl = template.get_schedule_services()
for f in pl:
    f["func"]()