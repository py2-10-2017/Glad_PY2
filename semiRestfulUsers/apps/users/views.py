# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	allusers = User.objects.all()
	context = {
		"allusers": allusers
	}
	return render(request,'users/index.html', context)

def new(request):
	return render(request,'users/new.html')

def create(request):
    errors = User.objects.user_validator(request.POST)

    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error,extra_tags=tag)
        return redirect('/users/new')

    else:
        User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'])

    user_id = str(User.objects.last().id)
    
    return redirect('/users/' + user_id)

def update(request, user_id):
    errors = User.objects.user_validator(request.POST)

    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error,extra_tags=tag)
        return redirect('/users/' + user_id + '/edit')

    else:
        u = User.objects.get(id=user_id)
        u.first_name = request.POST['fname']
        u.last_name = request.POST['lname']
        u.email_address = request.POST['email']

        u.save()
    
    return redirect('/users/' + user_id)

def show(request, user_id):

    curUser = User.objects.get(id=user_id)

    context = {
        "user": curUser
    }
	
    return render(request,'users/show.html', context)

def edit(request, user_id):
    curUser = User.objects.get(id=user_id)

    context = {
        "user": curUser
    }
    return render(request,'users/edit.html', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')