# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	return render(request,'amadon/index.html')

def buy(request):
	try:
		request.session['total']
	except KeyError:
		request.session['total'] = 0

	try:
		request.session['items']
	except KeyError:
		request.session['items'] = 0
	request.session['items'] = request.session['items'] + int(request.POST['quantity'])
	request.session['curTotal'] = int(request.POST['quantity']) * float(request.POST['product_id'])
	request.session['total'] = float(request.session['total']) + float(request.session['curTotal'])
	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon/checkout.html')

def clear(request):
	request.session.pop('items')
	request.session.pop('total')
	return redirect('/amadon')

