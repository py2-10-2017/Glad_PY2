# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
import random
# the index function is called when root is visited
def index(request):
	try:
		request.session['coin']
		request.session['act']
	except KeyError:
		request.session["coin"] = 0;
		request.session['act'] = []

	return render(request,'ninja_gold/index.html')

def getgold(request):
	time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

	# The random module has many useful functions. This is one that gives a random number in a range
	building = request.POST['building']
	if building == "farm":
		randomNum = random.randrange(10, 21)
		request.session["coin"] += randomNum;
		request.session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "cave":
		randomNum = random.randrange(5, 11)
		request.session["coin"] += randomNum;
		request.session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "house":
		randomNum = random.randrange(2, 6)
		request.session["coin"] += randomNum;
		request.session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "casino":
		randomNum = random.randrange(-50, 51)
		request.session["coin"] += randomNum;
		if randomNum >= 0:
			request.session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
		elif randomNum < 0:
			request.session["act"].append({'activity':"Lose {} golds".format(abs(randomNum)), 'class':'lose', 'date':time})
  	return redirect('/')