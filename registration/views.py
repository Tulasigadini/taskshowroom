from django.shortcuts import render, redirect,get_object_or_404
from .forms import TaskForm
from .models import Task

def home(request):
    return render(request, 'registration/home.html')

def services(request):
    return render(request,"registration/services.html")

def contact(request):
    return render(request,"registration/contact.html")


def task_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.all()
    return render(request, 'registration/task_list.html', {'tasks': tasks, 'search_query': search_query})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'registration/task_form.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'registration/task_form.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'registration/task_confirm_delete.html', {'task': task})


   
