
<require require="表示引入当前路径文件，require里面不要空格"/>

select u.work_code,hrm.hrm_department_name,u.nick,u.bank_card_numbers,u.apply_card_no,u.email,u.birthday,st.sys_code_text as status_name

from (
    require("base.sql")
) u
left join hrm_department hrm on u.hrm_department_id = hrm.hrm_department_id
left join sys_code st on st.sys_code_type = 'user_job_status' and st.sys_code = u.`status`

order by st.order_index,u.work_code asc
