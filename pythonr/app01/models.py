from django.db import models
from django.http import HttpResponse
from mpmath.ctx_mp_python import return_mpc


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
# class Role(models.Model):
#     caption = models.CharField(max_length=16)
class Department(models.Model):
    title= models.CharField(max_length=16)
    age = models.IntegerField(default=2)
