from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    '''Shows a home page'''
    todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': todo})


def details(request, todo_id):
    '''Shows details of each todo'''
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', {'todo': todo})


def delete(request, todo_id):
    '''Delete showed todo'''
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'todo deleted successfully', 'success')
    return redirect('home')


def create(request):
    '''Create a new todo'''
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'todo updated successfully', 'success')
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
