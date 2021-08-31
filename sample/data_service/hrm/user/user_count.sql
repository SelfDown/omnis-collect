<require require="表示引入当前路径文件，require里面不要空格"/>
select count(u.user_id) as `count`
from (
    require("base.sql")
) u

