from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    # URLs Categorias
    path('categorias', views.list_categories, name='list_categories'),
    path('categorias/adicionar/', views.add_category, name='add_category'),
    path('categorias/editar/<int:id_category>/', views.edit_category, name='edit_category'),
    path('categorias/excluir/<int:id_category>/', views.delete_category, name='delete_category'),
    # URLs Tarefas
    path('', views.list_tasks, name='list_tasks'),
    path('adicionar/', views.add_task, name='add_task'),
    path('editar/<int:id_task>/', views.edit_task, name='edit_task'),
    path('excluir/<int:id_task>/', views.delete_task, name='delete_task'),
]
