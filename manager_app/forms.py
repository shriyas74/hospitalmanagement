from django import forms
from manager_app.models import Managerinfo

class ManagerForm(forms.ModelForm):
    class Meta():
        model=Managerinfo
        exclude=['name', 'email', 'password', 'gender', 'image', 'isactive', 'isavailable', 'isqueue', 'mobile', 'dob', 'role_id']
