from django.urls import path
from . import views

app_name = 'credentials'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('logout', views.logout, name='logout'),
    path('new_page/', views.new_page_view, name='new_page'),
    path('show_form/', views.show_form, name='show_form'),

]
