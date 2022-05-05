select name,data
from file_data
union all
select 'local_sql_content.sql' as name,sql as data from sql_table
