from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.core.paginator import Paginator


def show(request):
    todo = Todo.objects
    todolist = Todo.objects.all()
    paginator = Paginator(todolist, 2) #분할 될 객체, 한 페이지당 담길 객체 수.
    page = request.GET.get('page')
    posts = paginator.get_page(page) #page의 번호를 받아 해당 page를 리턴함.
    return render(request, 'show.html', { 'todo': todo, 'posts': posts })

def new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            #이건 안 되나?
            form.save()
            return redirect('main:show')
    else:
        form = TodoForm()
    return render(request, 'new.html', { 'form': form })


def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('main:show')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit.html', {'todo': todo, 'form': form })


def delete(request, pk):
    del_todo = get_object_or_404(Todo, pk=pk)
    del_todo.delete()
    return redirect('main:show')