select *
from monitor_active_test

where

test_sql_code = {{test_sql_code}}

{% if active_test_id %}
    and active_test_id != {{active_test_id}}
{% endif %}