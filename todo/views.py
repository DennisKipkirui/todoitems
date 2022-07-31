from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import TodoItem

# Create your views here.

def home(request):
    todo = TodoItem.objects.all()
    return render(request, 'home.html', { 'todo_list': todo })


def add(request):
    title = request.POST["title"]
    todo = TodoItem.objects.create(title=title)
    todo.save()
    return redirect("home")

def delete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect("home")
