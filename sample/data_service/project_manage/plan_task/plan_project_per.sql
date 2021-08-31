select GROUP_CONCAT(CONCAT(c.project_name,"【",c.project_id,"】")) AS project_ids,b.date,a.user_id,sum(a.per) as current_sum
from plan_task a
left join weekdays_holidays b on b.date >= a.start_date  and b.date<= a.end_date
left join project c on a.project_id = c.project_id
where b.date >= {{start_date}}
    and b.date < {{end_date}}
    and a.user_id = {{user_id}}
    {% if plan_task_id %}
    and plan_task_id != {{plan_task_id}}
    {% endif %}
    and a.op_user = {{session_user_id}}

GROUP BY date
HAVING sum(a.per)+{{per}} > 100

