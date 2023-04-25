from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    # name = forms.CharField(max_length=50, required=True)
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'select2 form-select','placeholder': 'Employee'})
    )
    
    class Meta:
        model = Employee
        fields = ['employee']


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields=['first_name','last_name','comment','company']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First name'}), 'last_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter last name'}), 'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write comment'}),
            'company':forms.Select(attrs={'class': 'select2 form-select','placeholder': 'Employee'})}

class NewCompnayForm(forms.ModelForm):
    class Meta:
        model =Company
        fields=['name']
        widgets={'name':forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter name of Company"})}