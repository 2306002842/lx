项目简介
这是一个基于 Django 框架的入门学习项目，涵盖了 Django 的核心功能：模型（ORM）、视图、模板、路由、静态文件、表单处理以及第三方 API 调用等。项目通过多个示例页面演示了从数据库操作到前端渲染的完整流程。

目录结构
text
pythonr/
├── manage.py                  # Django 命令行工具
├── app01/                     # 主应用
│   ├── admin.py               # 后台管理注册
│   ├── apps.py                # 应用配置
│   ├── models.py              # 数据模型
│   ├── tests.py               # 测试
│   ├── views.py               # 视图函数
│   └── migrations/            # 数据库迁移文件
│       ├── 0001_initial.py
│       ├── 0002_role.py
│       ├── 0003_department_delete_role_alter_userinfo_age.py
│       └── 0004_rename_caption_department_title.py
└── templates/                 # HTML 模板
    ├── info_add.html
    ├── info_list.html
    ├── login.html
    ├── tpl.html
    ├── user_add.html
    ├── user_list.html
    └── weather.html
核心功能模块
1. 数据模型（models.py）
项目定义了两个模型：

模型	字段	说明
UserInfo	name, password, age	用户信息表
Department	title, age	部门表
python
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)

class Department(models.Model):
    title = models.CharField(max_length=16)
    age = models.IntegerField(default=2)
注意：models.py 中引入了 mpmath.ctx_mp_python.return_mpc，这是一个无关的导入，建议删除。

2. 视图函数（views.py）
视图函数	路由	功能
index	/	返回欢迎信息
user_list	/user/list/	渲染用户列表页
user_add	/user/add/	渲染添加用户页
weather	/weather/	调用 Open-Meteo API 获取成都天气
something	/something/	演示请求方法并重定向到百度
tpl	/tpl/	演示 Django 模板语法
login	/login/	用户登录（GET 显示表单，POST 验证）
orm	/orm/	演示 ORM 增删改查
info_list	/info/list/	用户信息列表
info_add	/info/add/	添加用户信息
info_delete	/info/delete/	删除用户信息
3. 模板（templates/）
3.1 login.html
登录表单，包含 CSRF 令牌，提交后由 login 视图处理。

3.2 tpl.html
演示 Django 模板语法：

变量渲染：{{ n1 }}

列表索引：{{ n2.0 }}

循环：{% for item in n2 %}

字典取值：{{ n3.name }}

对象列表遍历：{% for item in n4 %}

3.3 info_list.html
用户信息表格，支持删除操作（通过 GET 参数 nid）。

3.4 info_add.html
添加用户表单，提交到 /info/add/。

注意：info_add.html 中 <from> 应为 <form>，这是一个拼写错误，会导致表单无法提交。

3.5 user_list.html
使用 {% load static %} 加载静态文件（Bootstrap、jQuery、图片）。

3.6 weather.html
展示成都实时天气，数据来自 Open-Meteo API。

4. 数据库迁移
迁移文件记录了模型的变更历史：

迁移文件	操作
0001_initial.py	创建 UserInfo 模型
0002_role.py	创建 Role 模型
0003_...	创建 Department，删除 Role，修改 UserInfo.age 默认值
0004_...	将 Department.caption 重命名为 title
运行项目
环境要求
Python 3.x

Django 6.x

requests（用于天气 API）

安装依赖
bash
pip install django requests
初始化数据库
bash
python manage.py makemigrations
python manage.py migrate
启动开发服务器
bash
python manage.py runserver
访问 http://127.0.0.1:8000/ 查看首页。

路由配置建议
在 pythonr/urls.py 中配置以下路由：

python
from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.index),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('weather/', views.weather),
    path('something/', views.something),
    path('tpl/', views.tpl),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete),
]
已知问题与改进建议
info_add.html 拼写错误：<from> 应改为 <form>，否则表单无法提交。

models.py 无关导入：删除 from mpmath.ctx_mp_python import return_mpc。

login.html 中 style="..."：应替换为具体的样式，如 style="color:red;"。

views.py 重复导入：from django.shortcuts import render, HttpResponse, redirect 出现了两次，可合并。

orm 视图：每次访问都会创建重复数据，建议改为仅演示查询或使用 get_or_create。

安全性：密码明文存储，实际项目中应使用 make_password 加密。

静态文件配置：确保 STATICFILES_DIRS 和 STATIC_URL 正确配置，以便 {% static %} 正常工作。

学习要点总结
Django 项目结构（manage.py、settings.py、urls.py、wsgi.py）

模型定义与数据库迁移

ORM 增删改查（create、filter、all、update、delete）

视图函数与请求处理（GET/POST）

模板语法（变量、循环、条件、静态文件）

表单处理与 CSRF 保护

重定向与第三方 API 调用
