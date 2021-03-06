1. params 处理参数
=========================================
这是个非常常用的模块，程序正式执行前一些简单的校验。 **extend_param**  继承参数 和 **handler_params**  处理参数，这个三个大模块，都是来处理参数的，可根据不同情况进行配置。

params 主要处理请求字段和校验字段
对任何增删改查的请求，进行参数处理，一般校验字段是否为空，字段是否唯一等等


1.params  公共模块
>>>>>>>>>>>>>>>>>>>>>>
配置示例

    .. code-block:: yaml
     :caption: 角色删除index.yaml

     key: user_role_delete
     name: 用户删除角色
     module: 'model_delete'
     model: UserRole
     params:
       user_id_list:
         check:
           template: "{{user_id_list|must_list}}"
           err_msg: "用户不能为空"
     filter:
       user_id__in: user_id_list


       
2.template  请求字段赋值
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
params 下字段，写template 然后写jinja2 模板语句
示例：

    .. code-block:: yaml
     :caption: 项目ID 生产UUIDindex.yaml

     key: "project_save"
     module: 'model_save'
     params:
       project_id:
         template: "{{''|uuid}}"


.. note::

   **{{''|uuid}}** ,其中uuid 自定义jinja2 模板语法。生成uuid 。专门会有一章来介绍模板自定义函数。
   怎么获取当前时间、获取配置



常用的赋值方法
  .. code-block:: yaml
     :caption: 常用赋值template 

      1. {{session_user_id}} 获取当前登录用户ID 
      2. {{""|current_date_time}} 获取当前时间 %Y-%m-%d %H:%M:%S ，举例 2021-01-16 09:00:15 
      3. {{""|current_day}} 获取当前时间 "%Y-%m-%d ，举例 2021-01-16  
      4. {{password|md5}} 获取md5 值   
      5. {{""|uuid}} 获取UUID  
      6. {{password|des}} des 加密  
      7. {{"xxx"|get_key}} 获取application.properties配置文件的 的配置  




3.default  请求字段填写默认值
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
params 下字段，写default,然后填写值
示例：

    .. code-block:: yaml
     :caption: 项目ID 生产UUIDindex.yaml

     key: "project_save"
     http: true
     module: 'model_save'
     params:
       is_delete:
         default: "0"
     model: SysProjects

4.check 校验字段
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
params 下字段，写check ,字典进行验证
示例：

.. code-block:: yaml
 :caption: 用户ID 列表index.yaml

 key: user_role_delete
 name: 用户删除角色
 module: 'model_delete'
 model: UserRole
 params:
   user_id_list:
     check:
       template: "{{user_id_list|must_list}}"
       err_msg: "用户不能为空"

check 下支持的标签
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1. template 进行模板校验，如果值为True 表示通过，为False 表示失败
#. err_msg 如果返回False，错误信息提示。 **支持写jinja2 语句** 
#. service 请求一个服务，结果为 service_result 判断结果
   示例：

   .. code-block:: yaml
    :caption: 检查编码是否存在
    
    key: "project_save"
    http: true
    module: 'model_save'
    params:
      project_code:
        check:
          service:
            service: project.project_query
            project_code: project_code
          template: "{{service_result|length <=0 }}"
          err_msg: "【{{project_code}}】编码已经存在"

