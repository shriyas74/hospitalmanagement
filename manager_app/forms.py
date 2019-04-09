from django import forms
from manager_app.models import Managerinfo,Department,Member

class ManagerForm(forms.ModelForm):
    class Meta():
        model=Managerinfo
        exclude=['name', 'email', 'password', 'gender', 'image', 'isactive', 'isavailable', 'isqueue', 'mobile', 'dob', 'role_id']
class DepartmentForm(forms.ModelForm):
    class Meta():
        model=Department
        exclude=["department_id","department_name","department_strength","department_location","department_head"]
class MemberForm(forms.ModelForm):
    class Meta():
        model=Member
        exclude=["role_id",'member_id','member_first_name','member_last_name','member_address','member_phone','member_image','member_email','member_gender','member_status','member_dob',"member_password","member_department"]
