from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

from .models import *

from .forms import *




def index(request):
    return render(request, 'app/index.html')


def task(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task') 

    
    context = {'tasks':tasks , 'form':form}
    return render(request, 'app/task.html',context)