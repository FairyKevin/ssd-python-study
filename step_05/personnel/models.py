from django.db import models

# Create your models here.
class Staff(models.Model):
    id = models.CharField(max_length=6,primary_key=True)         # 员工id
    name = models.CharField(max_length=10)      # 员工姓名
    section = models.CharField(max_length=10)   # 所在部门
    position = models.CharField(max_length=10)  # 职位
    sex = models.CharField(max_length=2)        # 性别
    edu = models.CharField(max_length=10)       # 学历
    birthday = models.DateField()               # 出生日期
    entry = models.DateField()                  # 入职时间