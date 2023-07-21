from django import forms
from .models import Massage

class MassageForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True) 
    massage = forms.CharField(max_length=1000, required=True)  

    class Meta:
        model = Massage
        exclude = ()