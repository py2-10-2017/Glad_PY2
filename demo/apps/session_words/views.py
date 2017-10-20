# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def addword(request):
	time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
	try:
		request.session['words']
	except KeyError:
		request.session['words'] = []

	isBig = ''
	request.session['glad'] = request.session['glad']  + 'g'
	if( 'big' in request.POST):
		isBig = 'big'
	request.session['words'].append({'wordings': request.POST['newword'] + 'add on ' , 'class': request.POST['color'] + ' ' + isBig , 'date':time})
	print request.session['words']
	return redirect('/session_words')

def clear(request):
	request.session.pop('words')
	return redirect('/session_words')

def index(request):
	return render(request,'session_words/index.html')