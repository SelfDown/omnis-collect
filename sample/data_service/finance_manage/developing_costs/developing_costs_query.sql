<require require="表示引入当前路径文件，require里面不要空格"/>

SELECT c.*, p.project_name, d.hrm_department_name, d.hrm_department_arch FROM
(
require("base.sql")
) c
LEFT JOIN project p ON p.project_id = c.project_id
LEFT JOIN hrm_department d ON d.hrm_department_id = c.hrm_department_id

{% if pagination %}
    limit {{start_row}} ,{{ size }}
{% endif %}



