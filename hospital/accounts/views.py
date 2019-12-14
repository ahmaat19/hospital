from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignupModelForm, LoginModelForm, ChangePasswordModelForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# Create your views here.


@login_required
def Signup(request):
    form = SignupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {
        'form': form,
        'title': 'Signup Form',
        'valueBtn': 'Signup',
    }
    return render(request, 'accounts/signup.html', context)


def Login(request):
    if request.method == 'POST':
        form = LoginModelForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/dashboard/')
    else:
        form = LoginModelForm()
    context = {
        'form': form,
        'title': 'Login Form',
        'valueBtn': 'Login',
    }
    return render(request, 'accounts/login.html', context)


@login_required
def Logout(request):
    auth.logout(request)
    return render(request, 'index.html')


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordModelForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/dashboard/')
            messages.error(request, 'Change Password Success.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordModelForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form,
        'title': 'Change Password Form',
        'valueBtn': 'Change',
    })


@login_required
def ResetPassword(request):
    pass
