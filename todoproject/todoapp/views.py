from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'tsk1'


class TaskDetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    tsk1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        tsk = task(name=name, priority=priority, date=date)
        tsk.save()
    return render(request, "home.html", {'tsk1': tsk1})


# def details(request):
#
#     return render(request, 'detail.html',)

def delete(request, taskid):
    tsk = task.objects.get(id=taskid)
    if request.method == 'POST':
        tsk.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    tsk = task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=tsk)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'tsk': tsk})
