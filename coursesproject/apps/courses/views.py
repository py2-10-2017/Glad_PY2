# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	allcourse = Course.objects.all()
	context = {
		"courses" : allcourse
	}
	return render(request,'courses/index.html', context)

def add(request):
	errors = Course.objects.course_validator(request.POST)
	
	if errors:
		for tag, error in errors.iteritems():
			messages.error(request, error,extra_tags=tag)
	else:
		Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])

	return redirect('/')

def confirm(request, c_id):
	curCourse = Course.objects.get(id=c_id)

	context = {
        "course": curCourse
    }
	
	return render(request,'courses/confirm.html', context)

def delete(request, c_id):
	Course.objects.get(id=c_id).delete()
	return redirect('/')