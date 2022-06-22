from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('categorias', views.list_categories, name='list_categories'),
    path('categoria/adicionar/', views.add_category, name='add_category'),
    path('categoria/editar/<int:id_category>/', views.edit_category, name='edit_category'),
    path('categoria/excluir/<int:id_category>/', views.delete_category, name='delete_category'),    
]
