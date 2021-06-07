from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic import DetailView,UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class Taskdetailsview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskeditview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('Name', 'Priority','Date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def example(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('Task', '')
        Priority = request.POST.get('Priority', '')
        Date=request.POST.get('Date','')
        task = Task(Name=Name, Priority=Priority, Date=Date)
        task.save()
    return render(request, 'index.html', {'task': task1})


# def detailss(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})