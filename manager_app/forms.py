from django import forms
from manager_app.models import Managerinfo,Department

class ManagerForm(forms.ModelForm):
    class Meta():
        model=Managerinfo
        exclude=['name', 'email', 'password', 'gender', 'image', 'isactive', 'isavailable', 'isqueue', 'mobile', 'dob', 'role_id']
class DepartmentForm(forms.ModelForm):
    class Meta():
        model=Department
        exclude=["department_id","department_name","department_strength","department_location","department_head"]