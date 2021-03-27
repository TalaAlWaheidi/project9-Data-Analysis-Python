from django import forms  
from employee.models import Employee 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class SignupForm(UserCreationForm):
            class Meta:
                model = User
                fields = ['username','email','password1','password2']