select b.nick as op_user_name ,c.nick as username,d.hrm_department_name as first_department_name,
e.hrm_department_name as second_department_name,f.hrm_jobtitle_name,c.work_code,
a.*
from attendance_white_list a
left join user_account b on a.op_user = b.user_id
left join user_account c on a.user_id = c.user_id
left join hrm_department d on c.user_hrm_department_id_level2 = d.hrm_department_id
left join hrm_department e on c.user_hrm_department_id_level3 = e.hrm_department_id
left join hrm_jobtitle f on c.hrm_jobtitle_id =  f.hrm_jobtitle_id

where 1=1
{% if user_id %}
    and a.user_id = {{user_id}}
{% endif %}

{% if work_code %}
    and c.work_code = {{work_code}}
{%  endif %}

{% if ym %}
    and a.start_ym <= {{ym}} and  a.end_ym >= {{ym}}
{% endif %}
order by c.work_code