SELECT * FROM developing_costs c
WHERE 1=1
{% if project_id and project_id != '' %}
    AND c.project_id = {{project_id}}
{% endif %}
{% if hrm_department_id and hrm_department_id != '' %}
    AND c.hrm_department_id = {{hrm_department_id}}
{% endif %}
{% if start_date and start_date != '' and end_date and end_date != ''%}
    AND c.start_date >= {{start_date}}
    AND c.end_date <= {{end_date}}
{% endif %}
