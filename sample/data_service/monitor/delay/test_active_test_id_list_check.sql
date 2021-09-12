select *
from monitor_active_test
where active_test_id in ({{active_test_id_list}})
