select b.project_name,c.nick as username,c.work_code,
b.apply_department as project_department_id,
d.hrm_department_name as user_department_name,
c.hrm_department_id as user_department_id,
hb.hrm_department_name as project_department_name
,b.apply_department as project_department_id,
a.* from (
    require("base.sql")
) a
left join project b on a.project_id = b.project_id
left join hrm_department hb on b.apply_department = hb.hrm_department_id
left join user_account c on a.user_id = c.user_id
left join  hrm_department d on c.hrm_department_id = d.hrm_department_id
order by a.project_id, a.start_date