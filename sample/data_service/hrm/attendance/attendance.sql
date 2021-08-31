select a.userno,a.name,b.projectid,p.project_name,
case
when ifnull(onduty.allowance,0) >= ifnull(offduty.allowance,0) then ifnull(onduty.allowance,0)
else ifnull(offduty.allowance,0)
end as allowance
from attendance_archive_month a
join  attendance_archive_day b on a.attendance_archive_id = b.attendance_archive_id
left join province_city_allowance onduty on onduty.city_id = b.onduty_city_id
left join province_city_allowance offduty on offduty.city_id = b.offduty_city_id
left join project p on b.projectid = p.project_id
where a.ym = {{ym}} and b.attendance_type in ( 'CC','XCT','XCX')
order by a.userno
