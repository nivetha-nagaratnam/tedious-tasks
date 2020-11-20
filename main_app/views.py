from django.shortcuts import render, redirect
from .models import Task
from django.db.models import Sum

# Add the following import
from .forms import AddTaskForm
from django.views.generic.edit import DeleteView

def home(request):
  task_list = Task.objects.all()
  addtask1_form = AddTaskForm()
  form = AddTaskForm(request.POST)
  total_time = Task.objects.aggregate(Sum("time"))
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.save()
  return render(request, 'index.html', {'task_list':task_list,'addtask1_form': addtask1_form, 'total_time':total_time})

class TaskDelete(DeleteView):
  model = Task
  success_url = '/'


