from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm


class SignupModelForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=50)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=50)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), min_length=5)
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), max_length=50)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2', 'is_staff']


class ChangePasswordModelForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}), max_length=50)
    new_password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}), max_length=50)
    new_password2 = forms.CharField(label='Confirm Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), max_length=50)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class LoginModelForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
