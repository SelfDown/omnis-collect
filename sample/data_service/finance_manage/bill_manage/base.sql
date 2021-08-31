SELECT * FROM bill_manage m
WHERE 1=1
{% if bill_code and bill_code != '' %}
    AND m.bill_code = {{bill_code}}
{% endif %}
{% if user_id and user_id != '' %}
    AND m.user_id = {{user_id}}
{% endif %}
{% if start_date and start_date != '' and end_date and end_date != ''%}
    AND m.create_time >= {{start_date}}
    AND m.create_time <= {{end_date}}
{% endif %}

