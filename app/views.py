from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# Create your views here.

def home(request):
    context = {}

    if request.user.is_authenticated:
        context['task_list'] = Todo.objects.filter(author=request.user)
        return render(request, 'app/home.html', context)
    else:
        return render(request, 'app/home.html')

def add_task(request):
    new_task = Todo(author = request.user, content = request.POST['task'])

    new_task.save()
    return redirect('/home/')


def delete_task(request, task_id):
    task_to_be_deleted = Todo.objects.get(id = task_id)
    task_to_be_deleted.delete()
    return redirect('/home/')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'app/register.html', {'warning': 'Username already taken'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'app/register.html', {'warning': 'Email already taken'})   
        else:
            user = User.objects.create_user(username, email, password) 
            login(request, user)
            return redirect('/home/')

    else:
        return render(request, 'app/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'app/login.html', {'warning': 'Username or password didn\'t matched'})

    else:
        return render(request, 'app/login.html')


def user_logout(request):
    logout(request)
    return redirect('/home/')