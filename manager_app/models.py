from django.db import models


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=225, default="", unique=True)


class Managerinfo(models.Model):
    name = models.CharField(max_length=225, default="")
    email = models.CharField(primary_key=True, max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    mobile = models.CharField(max_length=225, default="")
    gender = models.CharField(max_length=225, default="")
    isactive = models.BooleanField(default=True)
    dob = models.CharField(max_length=225, default="")
    image = models.CharField(max_length=255, default="")
    isavailable = models.BooleanField(default=True)
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, default="")
    isqueue = models.BooleanField(default=True)