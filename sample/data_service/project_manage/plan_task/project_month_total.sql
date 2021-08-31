

    select project_id,project_name,DATE_FORMAT(date,'%%Y-%%m') as ym ,sum(day_count) as total_day,hrm_department_name   from (

        select c.project_id,c.project_name,b.date,a.per,a.user_id ,1*per*0.01 as day_count, h.hrm_department_name
        from plan_task a
        left join weekdays_holidays b on b.date >= a.start_date  and b.date<= a.end_date
        left join project c on a.project_id = c.project_id
        left join hrm_department h on c.apply_department = h.hrm_department_id
        where b.date >= {{start_date}}
        and b.date <={{end_date}}

    ) a

    GROUP BY project_id,month(date)
    order by project_id,month(date)
