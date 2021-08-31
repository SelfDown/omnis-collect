
select a.*,ROUND(total_day/month_days*100,2) as per from (
select a.*,
(select count(*) as count from weekdays_holidays b where b.date >= CONCAT(a.ym,"-01") and b.date <= CONCAT(a.ym,'-31')
) as month_days

from (
		select DATE_FORMAT(date,'%%Y-%%m') as ym ,sum(day_count) as total_day,hrm_department_name,user_id,nick ,work_code
		from (

				select b.date,a.per,a.user_id ,1*per*0.01 as day_count, h.hrm_department_name,c.nick,c.work_code
				from plan_task a
				left join weekdays_holidays b on b.date >= a.start_date  and b.date<= a.end_date
				left join user_account c on a.user_id = c.user_id
				left join hrm_department h on c.hrm_department_id = h.hrm_department_id
				where b.date >= {{start_date}}
                and b.date <={{end_date}}
                require("../require_test/t.sql")


		) a

		GROUP BY user_id,month(date)
		order by user_id,month(date)
) a
) a
