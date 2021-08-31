select u.*
from user_account u
left join sys_code st on st.sys_code_type = 'user_job_status' and st.sys_code = u.`status`
where u.work_code is not null

{% if work_code and work_code != '' %}
    and u.work_code = {{ work_code }}
{% endif %}
order by st.order_index,u.work_code asc

{% if pagination  %}
    limit {{start}} ,{{ size }}
{% endif %}