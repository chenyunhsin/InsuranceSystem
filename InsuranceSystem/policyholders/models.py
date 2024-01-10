from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator


class Policyholder(models.Model):
    id = models.AutoField(primary_key=True)
    # mockup 最大長度為10
    code = models.CharField(max_length=10,unique=True)
    # 目前台灣最長人名為25個字
    name = models.CharField(max_length=25)
    registration_date = models.DateTimeField(auto_now_add=True)
    # 第一位保險人的介紹人是null?
    introducer = models.ForeignKey('policyholders.Policyholder', on_delete=models.CASCADE,  related_name='policyholders',null=True)