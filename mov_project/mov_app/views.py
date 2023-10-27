from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForms
from .models import movie


# Create your views here.
def index(request):
    mov = movie.objects.all()
    context = {
        'movie_list': mov
    }
    return render(request, "index.html", context)


def details(request, movie_id):
    movi = movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movi})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movi = movie(name=name, desc=desc, year=year, img=img)
        movi.save()
    return render(request, 'add.html')


def update(request, id):
    movi = movie.objects.get(id=id)
    form = MovieForms(request.POST or None, request.FILES, instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form': form,'movie':movi})


def delete(request,id):
    if request.method =='POST':
        movi=movie.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')


