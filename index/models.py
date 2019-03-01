from django.db import models
from django.utils.html import format_html
from hos.models import Doctor, Office, Patient2


# # 创建产品信息表
# class Product(models.Model):
#     id = models.AutoField('序号', primary_key=True)
#     name = models.CharField('名称',max_length=50)
#     weight = models.CharField('重量',max_length=20)
#     describe = models.CharField('描述',max_length=500)
#     # 设置返回值
#     def __str__(self):
#         return self.name

