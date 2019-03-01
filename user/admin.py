# Register your models here.
# from django.contrib import admin
# from .models import *
# from django.contrib import messages

# # 将模型直接注册到admin后台
# admin.site.register(Patient)

# 修改title和header
# admin.site.site_title = '挂号系统后台管理登陆'
# admin.site.site_header = '挂号系统后台管理'


from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    pass
    # list_display = ['username', 'email', 'mobile', 'qq', 'weChat']
    # 新增用户时，在个人信息里添加'mobile','qq','weChat'的信息录入
    # 将源码的UserAdmin.fieldsets转换成列表格式
    # fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin的fieldsets，添加'mobile','qq','weChat'的信息录入
    # fieldsets[1] = (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile', 'qq', 'weChat')})