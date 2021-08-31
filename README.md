# omnis-collect
omnis-collect 是基于django框架，开发的一款web接口配置工具。目的是将系统的所有的接口都统一，简单点说，将所有的增删改查接口统一、让系统只有一个http接口，业务接口都是配置出来。
实现通过一些简单配置，可以提供http接口服务。

    目前已经实现
1. 路由配置。将接口分目录管理，可以相似业务模块的功能放在一个大目录，同一页面的接口功能放在一个文件
1. 模板查询。利用jinja2模板渲染+yml的语法。通过配置sql文件，实现根据配置sql 转http接口
1. 模型数据新增、修改、删除。利用django model的orm,实现对模型数据的新增、修改、删除
1. Excel文件下载。基于配置模板查询的数据，实现数据导出
1. Excel 文件导入更新。批量更新操作，数据库一次性执行
***

## 环境要求
+ 依赖要求 django 1.11.23,熟悉django 目录结构，django model 的使用
+ 系统中已经有sys_projects 项目表，并且有project_name 字段。其他业务表也行，这里是拿项目表举例
+ 根目录下必须有conf/application.properties.
  - application.propertes 配置 写下一下配置
  + collect_file_path=./omnis_data_service/service_router.yml   这个是路由入库文件，根据实际情况替换
+ 根据上一步的配置，必须在根目录下创建omnis_data_servcie目录并且新建service_router.yml

***
## 目录结构
+ conf
  + application.properties
+ sample
  + app 目录结构...
  + settings.py
+ omnis_data_service
  + service_router.yml
  
## 集成
### 安装依赖
    pip install omnis-collect --index-url https://pypi.org/simple
### 安装模块
settings.py 中安装模块
```
INSTALLED_APPS = [
     ... 其他模块
    'collect'

]
```
### 添加系统路由
找到urls.py 文件，可以根据自己需要调整路由，主要避免冲突
```
from django.conf.urls import include
urlpatterns = [
    ... 其他模块
    url(r'^excel_manage/', include("collect.urls")),
    url(r'^template_data/', include("collect.template_urls")),
]

```
## 添加示例
### 添加项目查询
#### 添加总路由
首先在service_router.yml 写下如下配置。这个文件是总路由文件。如果已经存在内容就只要更内容
```dart
# 系统总路由
services:
  - key: 'hrm'
    name: '人资模块'
    path: 'hrm/service.yml'
  - key: 'project_manage'
    name: '项目管理'
    path: 'project_manage/service.yml'
  - key: 'man_hour_manage'
    name: '工时管理'
    path: 'man_hour/service.yml'
  - key: 'finance'
    name: '财务管理'
    path: 'finance_manage/service.yml'
  - key: 'common'
    name: '权限'
    path: 'common/service.yml'

# 返回结果转换规则
rules:
  excel:
    path: "collect.service_imp.rules.data_2_excel_rule"
    class_name: "Data2ExcelRule"
# SQL 模板关键字规则
key_word_rules:
  require:
    path: collect.service_imp.key_word_rules.require
    class_name: Require
    reg: require[(](.*?)[)]


# 请求参数处理规则
request_rules:

  # 字符串format
  - name: format
    path: collect.service_imp.request_rules.format
    class_name: Format
  # 表达式
  - name: exp
    path: collect.service_imp.request_rules.exp
    class_name: Expression
  # 模板渲染
  - name: template
    path: collect.service_imp.request_rules.template
    class_name: TemplateData
  # 检查数据
  - name: check
    path: collect.service_imp.request_rules.check
    class_name: CheckData

# django 模型配置
django_model:
  # django model 文件位置
  model_file: sample.models.models
# 缓存
cache:
  # 默认60s
  max: 60
  # 获取django 的默认缓存对象
  path: django.core.cache
  obj: cache

# 请求处理器
request_handler:
  # 字段转数组
  - key: field2array
    path: collect.service_imp.request_handlers.handlers.field2array
    class_name: Field2Array
    method: handler
  # 服务转字段
  - key: service2field
    path: collect.service_imp.request_handlers.handlers.service2field
    class_name: Service2Field
    method: handler
  # 忽略数据
  - key: update_data
    path: collect.service_imp.request_handlers.handlers.update_data
    class_name: UpdateData
    method: handler
  # 更新数据
  - key: ignore_data
    path: collect.service_imp.request_handlers.handlers.ignore_data
    class_name: IgnoreData
    method: handler

# 结果处理器
result_handler:
  # 列转行
  - key: row2col
    path: collect.service_imp.result_handlers.handlers.row2col
    class_name: Row2Col
    method: handler

  # 合并列
  - key: combine
    path: collect.service_imp.result_handlers.handlers.combine
    class_name: Combine
    method: handler
  # 排序
  - key: arrsort
    path: collect.service_imp.result_handlers.handlers.array_sort
    class_name: ArraySort
    method: handler
  # 取树形节点，一级节点二级节点名称
  - key: tree_node_name
    path: collect.service_imp.result_handlers.handlers.tree_node_name
    class_name: TreeNodeName
    method: handler
# 模块处理器
module_handler:
  # mysql 查询
  - key: mysql
    path: collect.service_imp.mysql.mysql_service
    class_name: MysqlService
  # mysql 更新
  - key: mysql_update
    path: collect.service_imp.mysql.mysql_update
    class_name: MysqlUpdateService
  # 模型保存
  - key: model_save
    path: collect.service_imp.model.model_save
    class_name: ModelSaveService
  #  模型删除
  - key: model_delete
    path: collect.service_imp.model.model_delete
    class_name: ModelDeleteService
  # 模型保存
  - key: bulk_create
    path: collect.service_imp.model.bulk_create
    class_name: BulkCreateService

filter_handler:
  # uuid
  - key: uuid
    path: collect.service_imp.common.filters.template_filters.uuid
    class_name: UUIDFilter
    method: filter
  # 创建日期
  - key: current_date_time
    path: collect.service_imp.common.filters.template_filters.date_time
    class_name: CurrentDateTime
    method: filter
  # 判断记录是否存在
  - key: exist
    path: collect.service_imp.common.filters.template_filters.exist
    class_name: ExistFilter
    method: filter
  # 必须是数组
  - key: must_list
    path: collect.service_imp.common.filters.template_filters.must_list
    class_name: MustListFilter
    method: filter
  # 必传
  - key: must
    path: collect.service_imp.common.filters.template_filters.must
    class_name: MustFilter
    method: filter
  #  循环数组，取字符串
  - key: foreach
    path: collect.service_imp.common.filters.template_filters.foreach
    class_name: ForeachFilter
    method: filter
  # 判断对象是否在数组里面
  - key: in_array
    path: collect.service_imp.common.filters.template_filters.in_array
    class_name: InArrayFilter
    method: filter


```
要改的地方
1. servcies 表示服务模块，如果要加模块就在这里
1. django_model 表示模型位置，model_file 模型位置，根据项目不同自行替换

#### 添加项目目录
根据services 下的 project_manage 配置，必须创建project_manage/service.yml
创建 project_mange 目录，然后创建service.yml
#### 关联子模块。
修改project_manage/servcie.yml。这个文件主要做管理各个目录来用。

  ```dart
    #项目点路由
    service:
      - name: "项目模块"
      path: "project/index.yml"

  ```
path 指向具体服务路径
#### 配置子路由
1.创建project,以及新建index.yml
2.在index.yml配置

```python

service:
  # 项目
  - key: "project"
    module: 'mysql'# 执行mysql 查询
    sql_file: 'project.sql'
    result_parse: "excel"
    data_type: 'file'
    excel_out_path: './attendance_out/project.xls'
    file_name: '项目模板.xls'
    excel:
      0:
        start_row: 2
        data: result
        fields:
          - name: 项目名称
            value: project_name
          - name: 编码
            value: project_code
```
注意 excel_out_path配置的 attendance_out目录必须存在，文件会自动创建
3.创建project.sql 文件，编写sql 

```
   select * 
   from sys_projects
   limit 10
```
前提数据库必须有sys_projects 表，如果没有，请在数据库中手动执行

```

CREATE TABLE sys_projects  (
  sys_project_id varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  project_name varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  project_code varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (sys_project_id) USING BTREE,
  INDEX sys_project_id(sys_project_id) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

```
#### 测试服务
接口地址 /omnis 是我的项目设置的一级路由，根据实际情况替换，template_data 是文档“集成”步骤的路由

```/omnis/template_data/data```
post body 发送

```
{ 
   "service":"project_manage.project"
 }
```

返回结果

```dart
{
  "msg": "成功",
  "code": "0",
  "data": [
    {
      "zabbix_service_id": 1,
      "project_name": "全部项目",
      "git_branch_sql": "comm",
      "zabbix_max_maintenance_time": 30,
      "selected": "True",
      "order_id": 2,
      "sys_project_id": "-1",
      "comments": null,
      "project_leader": null,
      "flag_del": null,
      "porject_name_sql": "产品",
      "modify_time": "2020-09-28 15:06:52",
      "create_time": "2018-03-28 16:01:14",
      "notes": null,
      "server_ip": "192.168.20.163",
      "site": "http://www.tjhcc.com.cn:100/",
      "wechat_id": 1,
      "project_code": "ALL",
      "jiraspace": null
    }
  ],
  "success": true
}
```

下载excel
/omnis/excel_manage/download?service=project_manage.project

[接口文档地址](http://wiki.cenboomh.com:88/pages/viewpage.action?pageId=59092313)
