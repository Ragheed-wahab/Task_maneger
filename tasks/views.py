from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    tasks= Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        tit = request.POST.get('title')
        desc = request.POST.get('description')
        st = request.POST.get('state') == 'on'
        dt = request.POST.get('date')
        if (tit and desc) and dt :
            new_task = Task(title=tit, description=desc, deadline =dt, completed =st)
            new_task.save()
        return redirect('task_list')
    return render(request,'tasks/add_task.html')
def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('task_list')
