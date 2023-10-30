from django.http import HttpResponse
from django.shortcuts import render

from .models import travel
from .models import travel_end


# Create your views here.
def demo(request):
    obj = travel.objects.all()
    objj = travel_end.objects.all()
    return render(request, "index.html", {'result': obj,'end': objj})



