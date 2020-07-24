from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='required.')
    phone = forms.CharField(max_length=30, required=True, help_text='requred.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'phone', 'email', 'password1', )
