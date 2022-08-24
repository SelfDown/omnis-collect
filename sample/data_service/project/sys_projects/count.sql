select count(*) as count
from sys_projects a
where 1=1
{% if project_code %}
    and a.project_code = {{project_code}}
{% endif  %}

{% if sys_project_id_list %}
    and a.sys_project_id in ({{sys_project_id_list}})
{% endif %}

{% if exclude %}
    and a.sys_project_id != {{exclude}}
{% endif %}
{% if project_list %}
   and (a.project_name,a.project_code) in(
      {% for project in project_list %}({{project.project_name}},{{project.project_code}}) {% if not loop.last  %},{% endif %}
      {% endfor %}
   )
{% endif %}
{% if pagination %}
  limit 10
{% endif %}