from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, TaskForm
from .models import Category, Task


def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso!')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)


def list_categories(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

def edit_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

