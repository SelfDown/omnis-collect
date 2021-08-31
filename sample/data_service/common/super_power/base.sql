select 1
from  user_role_id_list  a
join user_role  b on a.role_id = b.role_id
where b.role_code = {{super_user_code}} and a.user_id = {{user_id}}
