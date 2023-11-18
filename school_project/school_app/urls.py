from django.urls import path

from school_app import views
from school_app.views import department_view

urlpatterns = [
    path('',views.demo,name='demo'),
    path('department/<str:department_name>/', department_view, name='department_view'),
]