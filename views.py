from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User

def index(request):
    user_list = User.objects.all()
    context = {
        'users': user_list
    }
    return render(request, "sr_users/index.html", context)

def user(request, id):
    context = {
        'users': User.objects.filter(id=id)
    }
    print context
    return render(request, "sr_users/user.html", context)

def new(request):
    User.objects.validate_new(request)
    return render(request, "sr_users/new.html")

def edit(request, id):
    User.objects.validate_edit(request, id)
    user_list = User.objects.filter(id=id)
    context = {
        'users': user_list
    }
    return render(request, "sr_users/edit.html", context)

def destroy(request, id):
    User.objects.delete(request, id)
    return redirect("/sr_users")
    
