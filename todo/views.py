from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
# Create your views here.
def index(requset):
    todo = Todo.objects.all()
    return render(requset, "todo/index.html", {"todo":todo})