select att.sys_code_text as type_name,att.property_1 as type_icon , c.server_ip,b.db_schema,d.user_name,a.*
from (require("active_test_base.sql")) a
left join server_install_soft b on a.test_install_soft_id = b.install_soft_id
left join server_soft_user d on a.soft_user_id = d.soft_user_id
left join server_instance c on b.server_id = c.server_id

left join sys_code att on att.sys_code_type = 'active_test_type' and a.test_type = att.sys_code


