# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

  # the index function is called when root is visited

def index(request):
	if "attmp" not in request.session: 
		request.session["attmp"] = 0;
	request.session["attmp"] = request.session["attmp"] + 1
	context = {
	"randNum": get_random_string(length=14)
	}
	return render(request,'random_word/index.html', context)

def reset(request):
	if "attmp" in request.session: 
		request.session["attmp"] = 0;
	return redirect('/random_word')
