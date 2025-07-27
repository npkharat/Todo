from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-update_at')
    
    completed_task = Task.objects.filter(is_completed = True)
    context ={
        'tasks':tasks,
        'completed_task':completed_task
    }
   
    return render(request, 'home-todo.html', context)

def add_todo(request):
        task = request.POST['task']
        if task :
            Task.objects.create(task=task)
        return redirect('home')

def mark_as_done(request,pk):
     task = get_object_or_404(Task,pk=pk)
     task.is_completed = True
     task.save()
     return redirect(home)
def mark_as_undone(request,pk):
     task = get_object_or_404(Task,pk=pk)
     task.is_completed = False
     task.save()
     return redirect(home)

def delete_task(request,pk):
     task = get_object_or_404(Task,pk=pk)
     task.delete()
     return redirect(home)
     
def edit_task(request,pk):
     task = get_object_or_404(Task,pk=pk)
     context={
          'task':task
     }
     if request.method == 'POST':
          updated_task = request.POST['task']
          task.task= updated_task
          task.save()
          return redirect('home')
     else:
          return render(request, 'edit.html', context)