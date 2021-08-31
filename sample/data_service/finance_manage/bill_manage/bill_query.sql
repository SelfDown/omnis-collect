<require require="表示引入当前路径文件，require里面不要空格"/>

SELECT m.*, u.nick as user_name, u.work_code FROM
(
require("base.sql")
) m
LEFT JOIN user_account u ON u.user_id = m.user_id

ORDER BY m.create_time DESC
{% if pagination %}
    limit {{start_row}} ,{{ size }}
{% endif %}



