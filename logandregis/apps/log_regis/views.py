# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
import bcrypt

  # the index function is called when root is visited
def index(request):
	return render(request,'log_regis/index.html')

def regis(request):
	errors = User.objects.regis_validator(request.POST)

	if errors:
		for tag, error in errors.iteritems():
			messages.error(request, error,extra_tags=tag)
		return redirect('/')

	else:
		User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt()))
		curRegis = User.objects.last()
		context = {
			"curRegis": curRegis
		}

		return render(request,'log_regis/success.html', context)

def login(request):
	errors = User.objects.login_validator(request.POST)

	if errors:
		for tag, error in errors.iteritems():
			messages.error(request, error,extra_tags=tag)
		return redirect('/')

	else:
		curRegis = User.objects.get(email=request.POST["email"])
		context = {
			"curRegis": curRegis
		}

		return render(request,'log_regis/success.html', context)