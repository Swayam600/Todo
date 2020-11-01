from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home-page'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('register/', views.user_register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout')
]
