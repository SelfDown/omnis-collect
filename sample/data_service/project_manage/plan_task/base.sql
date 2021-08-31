select timestampdiff(day,a.start_date,a.end_date)+1 as duration,a.*
from plan_task a
where 1=1
{% if start_date  and end_date %}
<ps 处理左中/>
<ps 任务开始日期 大于 查询开始日期 并且 日期的开始日期 小于查询的结束日期,/>
    and (
    ( a.start_date >= {{start_date}} AND a.start_date <= {{end_date}} )
     <ps 处理包含/>
     <ps 任务的开始日期小于 查询的开始日期,任务的结束日期小于查询的结束日期.>

      OR ( a.start_date <= {{start_date}}  AND a.end_date >={{end_date}})
     <ps 处理右中/>
     OR ( a.end_date >=  {{start_date}} and a.end_date <={{end_date}} )

 )
{% endif %}
and a.op_user = {{session_user_id}}

{% if pagination %}
    limit {{start_row}} ,{{ size }}
{% endif %}