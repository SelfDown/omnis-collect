# -*- coding: utf-8 -*-
from collect.service.template_service import TemplateService
import collect.service_imp.common.filters.template_filters.date_time
template = TemplateService(op_user="sys")
pl = template.get_schedule_services()
for f in pl:
    f["func"]()