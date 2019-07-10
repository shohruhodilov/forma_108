from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms




class UserRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, label='Phone number')
    inn = forms.CharField(max_length=15, label='INN')
    address = forms.CharField(widget=forms.Textarea (attrs={"rows":5, "cols":10}), label='Your Address')

    class Meta:
        model = User
        fields = ['username','phone', 'inn', 'address', 'password1','password2']