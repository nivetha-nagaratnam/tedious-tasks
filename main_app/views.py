from django.shortcuts import render, redirect
from .models import Task

# Add the following import
from .forms import AddTaskForm
from django.views.generic.edit import DeleteView

def home(request):
  task_list = Task.objects.all()
  addtask1_form = AddTaskForm()
  form = AddTaskForm(request.POST)
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.save()
  return render(request, 'index.html', {'task_list':task_list,'addtask1_form': addtask1_form})

class TaskDelete(DeleteView):
  model = Task
  success_url = '/'


