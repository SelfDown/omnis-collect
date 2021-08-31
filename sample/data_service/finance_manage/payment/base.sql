select * from (

    select a.payment_flow_id,wf_no,wf_cost_sum as money ,
    CASE
            WHEN u.nick is null THEN
                    a.wf_payee
            ELSE
                    u.nick
	END username,  u.work_code,a.create_time as finish_time,
    pd.bank_no as pay_card_num,pd.cost_time,pd.sno,
    CASE
    WHEN ifnull(a.payment_detail_id,"") ="" THEN
            'not_sure'
    ELSE
            'sure'
    END flow_status,
    CASE
    WHEN ifnull(a.payment_detail_id,"") ="" THEN
            '未确认'
    ELSE
            '已确认'
    END flow_status_text,
    d.hrm_department_id,
	  d.hrm_department_name,
	  a.project_id,
    p.project_name
    from (
        select a.*
        from payment_flow a

        {% if hrm_department_id and hrm_department_id != '' %}
          LEFT JOIN user_account u ON a.wf_payee = u.user_id
        {% endif %}

        where 1=1


         <ps 对公/>
        {% if public_self and public_self == '0' %}
            and ifnull(a.wf_bank_card,'') = ''
        <ps 个人 />
        {% elif public_self and public_self == '1' %}
            and ifnull(a.wf_bank_card,'') != ''
        {% endif %}
        <ps 流程审批时间 />
        {% if start and start != '' and end != ''%}
            and a.create_time >= {{start_time}} and a.create_time <= {{end_time}}
        {% endif %}
         <ps 领款人 />
        {% if user_id and user_id != '' %}
            and a.wf_payee = {{user_id}}
        {% endif %}
        <ps 金额>
        {% if money and money != '' %}
            and a.wf_cost_sum = {{money}}
        {% endif %}

        {% if search and search != '' %}

            and a.wf_no like {{search}}
        {% endif %}

        {% if show_model and show_model == 'self' %}
            and  a.wf_payee = {{session_user_id}}
        {% endif %}


        {% if hrm_department_id and hrm_department_id != '' %}
            AND ( u.hrm_department_id = {{hrm_department_id}} OR u.user_hrm_department_id_level2 = {{hrm_department_id}} OR u.user_hrm_department_id_level3 = {{hrm_department_id}} )
        {% endif %}


        {% if project_id and project_id != '' %}
            AND a.project_id = {{project_id}}
        {% endif %}





        order by a.create_time  desc


    ) a
    left join payment_detail pd on pd.payment_detail_id = a.payment_detail_id
    left join user_account u on a.wf_payee = u.user_id
	  LEFT JOIN hrm_department d ON d.hrm_department_id = u.hrm_department_id
	  LEFT JOIN project p ON p.project_id = a.project_id
    <ps 对公不显示  匹配项目不显示 />
    {% if public_self and public_self == '0' %}
    {% if not project_id or project_id == '' %}

        UNION all
        select
        '' as payment_flow_id,'' as wf_no,pd.cost_total as money ,
        payee as username,''as work_code,  pd.cost_time as  finish_time,
        pd.bank_no as pay_card_num,pd.cost_time,pd.sno  ,
        'not_match' as flow_status,
        '未匹配' as flow_status_text,
        d.hrm_department_id,
	      d.hrm_department_name,
	      '' AS project_id,
		    '' AS project_name
        from (
                select pd.*
                from payment_detail pd
                {% if show_model == 'self' or user_id != '' or hrm_department_id  != '' %}
                    left join user_account u on pd.payee = u.nick
                {% endif %}
                where pd.payment_flow_id is null

                {% if start and start != '' and end != ''%}
                    and pd.cost_time >= {{start_date}} and pd.cost_time <= {{end_date}}
                {% endif %}
                <ps 领款人 />
                {% if user_id and user_id != '' %}
                 and  u.user_id = {{user_id}}
                {% endif %}

                {% if money and money != '' %}
                    and pd.cost_total = {{money}}
                {% endif %}

                {% if search and search != '' %}

                    and 1 != 1
                {% endif %}


                {% if show_model and show_model == 'self' %}
                    and  u.user_id = {{session_user_id}}
                {% endif %}

                {% if hrm_department_id and hrm_department_id != '' %}
                    AND ( u.hrm_department_id = {{hrm_department_id}} OR u.user_hrm_department_id_level2 = {{hrm_department_id}} OR u.user_hrm_department_id_level3 = {{hrm_department_id}} )
                {% endif %}

            ) pd
            LEFT JOIN user_account u ON pd.payee = u.nick
				    LEFT JOIN hrm_department d ON d.hrm_department_id = u.hrm_department_id
    {% endif %}
    {% endif %}
) a
{% if flow_status and flow_status != '' %}
    WHERE a.flow_status = {{flow_status}}
{% endif %}

order by a.finish_time desc

{% if pagination %}
    limit {{start_row}} ,{{ size }}
{% endif %}











