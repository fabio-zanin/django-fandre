from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserForm, UserFormChangeInformation, UserProfileForm
from .models import UserProfile


def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário salvo com sucesso!')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


def login_user(request):
    template_name = 'accounts/login_user.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, template_name, {})


@login_required(login_url='contas/login/')
def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')


@login_required(login_url='contas/login/')
def password_change_user(request):
    template_name = 'accounts/password_change_user.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Senha atualizada com sucesso.")
            update_session_auth_hash(request, form.user)
        else:
            messages.error(request, "Não foi possível atualaizar a senha!")
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='contas/login')
def add_profile_user(request):
    template_name = 'accounts/add_profile_user.html'
    context = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, "Perfil alterado como sucesso!")
    form = UserProfileForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='contas/login')
def list_profile_user(request):
    template_nome = 'accounts/list_profile.html'
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    context ={
        'profile': profile
    }    
    return render(request, template_nome, context)


@login_required(login_url='contas/login')
def change_profile_user(request, username):
    template_name = 'accounts/add_profile_user.html'
    context = {}
    profile = UserProfile.objects.get(user__username=username) # __ lookup
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
    form = UserProfileForm(instance=profile)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='contas/login')
def change_information_user(request, username):
    template_name = 'accounts/change_information_user.html'
    context = {}
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UserFormChangeInformation(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações atualizadas com sucesso.")
    form = UserFormChangeInformation(instance=user)
    context['form'] = form
    return render(request, template_name, context)
