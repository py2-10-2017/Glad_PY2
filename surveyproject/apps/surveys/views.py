# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

  # the index function is called when root is visited
def index(request):
	return render(request,'surveys/index.html')

def process(request):
	request.session['fname'] = request.POST['fname'];
	request.session['location'] = request.POST['location'];
	request.session['language'] = request.POST['language'];
	request.session['comment'] = request.POST['comment'];

	if "attmp" not in request.session: 
		request.session["attmp"] = 0;
		
	request.session["attmp"] = request.session["attmp"] + 1
	return redirect('/result')

def result(request):
	return render(request,'surveys/result.html')