select a.*
from monitor_active_test a
{% if target_ip %}
left join server_install_soft b on a.test_install_soft_id = b.install_soft_id
left join server_instance c on b.server_id = c.server_id
{% endif %}
where
a.test_type in (3,6)
{% if active_test_name %}
    and active_test_name like {{active_test_name}}
{% endif %}
{% if target_ip %}
    and c.server_ip like {{target_ip}}
{%  endif %}


{% if test_type %}
    and test_type = {{test_type}}
{% endif %}

order by add_time desc

{% if pagination %}
    limit {{start_row}} ,{{ size }}
{% endif %}
