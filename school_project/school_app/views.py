from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    return render(request,'base.html')

def department_view(request, department_name):
    return redirect(f'https://en.wikipedia.org/wiki/{department_name}')