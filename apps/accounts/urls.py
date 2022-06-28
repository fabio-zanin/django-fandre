from pathlib import Path

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.login_user, name='login_user'),
    path('alterar-senha/', views.password_change_user, name='password_change_user'),
    path('novo-perfil/', views.add_profile_user, name='add_profile_user'),
    path('meu-perfil/', views.list_profile_user, name='list_profile_user'),
    path('aletrar-perfil/<username>/', views.change_profile_user, name='change_profile_user'),
    path('aletrar-usuario/<username>/', views.change_information_user, name='change_information_user'),
    path('sair/', views.logout_user, name='logout_user'),
]
