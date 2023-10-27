from django.urls import path

from mov_app import views

app_name = 'mov_app'  # namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]
