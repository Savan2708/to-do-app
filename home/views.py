from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            tasks = List.objects.all
            messages.success(request, 'Task Has Been Added To List...!!!')
            return render(request, 'home/home.html', {'tasks': tasks})
    else:
        tasks = List.objects.all
        return render(request, 'home/home.html', {'tasks': tasks})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Task Has Been Deleted...!!!')
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task Has Been Edited...!!!')
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'home/edit.html', {'item': item})
