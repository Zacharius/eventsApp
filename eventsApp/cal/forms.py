#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=150,required=False, widget=forms.TextInput(
        attrs ={
                'style': 'border-color: blue;',
                'placeholder': 'username'
            }
    ))
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'style': 'border-color: blue;',
            'placeholder': 'valid email'

        }
    ))
    password1 = forms.CharField(min_length=6, max_length=20,required=False, widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'style': 'border-color: blue;',
            'placeholder': 'password'
        }
    ))
    password2 = forms.CharField(min_length=6, max_length=20,required=False, widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'style': 'border-color: blue;',
            'placeholder': 'Confirm password'

        }
    ))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
