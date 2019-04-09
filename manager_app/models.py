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

class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=225)
    department_strength=models.IntegerField(null=True)
    department_location=models.CharField(max_length=225)
    department_head=models.CharField(max_length=225)

class Member(models.Model):
    role_id=models.ForeignKey(UserRole,on_delete=models.CASCADE,default="",null=True)
    member_id=models.AutoField(primary_key=True)
    member_first_name=models.CharField(default="",max_length=224,null=True)
    member_last_name=models.CharField(default="",max_length=225,null=True)
    member_address=models.CharField(default="",max_length=224)
    member_email=models.EmailField(default="",max_length=224)
    member_phone=models.CharField(default="",max_length=225)
    member_image=models.CharField(default="",max_length=225,null=True)
    member_gender=models.CharField(default="",max_length=225)
    member_status=models.BooleanField(default=True)
    member_dob=models.DateField(null=True)
    member_password=models.CharField(null=True,max_length=225)
    member_department=models.ForeignKey(Department,on_delete=models.CASCADE,default="",null=True)