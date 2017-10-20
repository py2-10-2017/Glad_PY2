# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  
def new(request):
	response = "placeholder for users to add a new survey"
	return HttpResponse(response)

def create(request):
	response = "placeholder to display all the surveys created"
	return HttpResponse(response)