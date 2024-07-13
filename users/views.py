from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User # type: ignore
from todos.models import *
from django.shortcuts import get_object_or_404
from todos.models import Todo
from .forms import NewTodoForm
from django.http import HttpResponseRedirect

from django.http import JsonResponse
import json

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users_list')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def user_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('login')  # You can redirect to any page after logout




def new_todos(request,user_id):
    if request.method == 'POST':
        form = NewTodoForm(request.POST)
        if form.is_valid():
            print(user_id)
            user = User.objects.get(pk=user_id)
            new_todos = form.save(commit=False)
            new_todos.user = user
            new_todos.save()
            print(new_todos)
            return redirect('todos',user_id)  # Yönlendirilecek URL'yi belirtin
    else:
        form = NewTodoForm()
    
    return render(request, 'new_todo.html', {'form': form})

def todos(request, user_id):
    user = User.objects.get(pk=user_id)
    todos = Todo.objects.filter(user_id=user_id).values()
    
    
    return render(request, 'user_todos.html', {'todos': todos, 'user': user})

from django.http import JsonResponse

def toggle_todo_state(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=todo_id)
        todo.is_completed = not todo.is_completed
        todo.save()
        data = {
            'is_completed': todo.is_completed
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
    
def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

def change_todo(request, todo_id):
    
    if request.method == 'POST':
        todo = Todo.objects.get(pk=todo_id)
        data = request.body
        data_dict = json.loads(data.decode("utf-8")) 
        todo.title = data_dict.get('title')
        todo.date_line = data_dict.get('date_line')
        todo.save()
        data={
            "title":todo.title,
            "date_line":todo.date_line
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
