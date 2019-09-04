from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f'User {username} successfully logged in'))
            return redirect('home')
            #return render(request, 'authenticate/home.html', {'username': username})
        else:
            messages.success(request, (f'Login failed!'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, (f'Logged out successfully'))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f"Welcome {username}"))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, (f"Profile Successfully Changed"))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit.html', context)


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, (f"Password Successfully Changed"))
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)