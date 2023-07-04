from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("s/",views.services,name="services"),
    path("c/",views.contact,name="contact"),
    path('t/', views.task_list, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/<int:pk>/', views.update_task, name='update_task'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
    

]
