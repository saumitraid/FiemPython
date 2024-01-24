from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import MyUser

class MyRegFrm(UserCreationForm):
    username=forms.CharField(label="Username",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter user name'}))
    first_name=forms.CharField(label="First Name",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter first name'}))
    last_name=forms.CharField(label="Last Name",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter last name'}))
    email=forms.CharField(label="Email-ID",
            widget=forms.EmailInput(attrs={'class':'form-control border-primary','placeholder':'Enter Email ID'}))
    mobile=forms.CharField(label="Contact Number",
            widget=forms.NumberInput(attrs={'class':'form-control border-primary','placeholder':'Enter contact number'}))
    address=forms.CharField(label="Address",
            widget=forms.Textarea(attrs={'class':'form-control border-primary','placeholder':'Enter your address'}))
    password1=forms.CharField(label="Password",
            widget=forms.PasswordInput(attrs={'class':'form-control border-primary','placeholder':'Enter your password'}))
    password2=forms.CharField(label="Confirm Password",
            widget=forms.PasswordInput(attrs={'class':'form-control border-primary','placeholder':'Enter your confirm password'}))
    class Meta:
        model = MyUser
        fields = ("username", 'first_name', 'last_name', 'email', 'mobile', 'address')