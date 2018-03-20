# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random, time, datetime

# Create your views here.

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activities_log' not in request.session:
		request.session['activities_log'] = []
	return render(request, "ninja_gold_app/index.html")

def process(request):
	# Pulling from POST
	building = request.POST['building']
	# Creating a list of buildings
	buildingsList = [['farm', random.randint(10, 20)],['cave', random.randint(5, 10)],['house', random.randint(2, 5)],['casino', random.randint(-50,50)]]
	# Capturing the current time
	timestamp = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
	for i in range(0,len(buildingsList)):
		if building == buildingsList[i][0]:
			request.session['gold'] = request.session['gold'] + buildingsList[i][1]
			if buildingsList[i][1] >= 0:
				request.session['activities_log'].append(['pos','Earned '+ str(buildingsList[i][1]) + ' gold from the '+str(building)+ '! ' + str(timestamp)])
				request.session.modified = True
			else:
				request.session['activities_log'].append(['neg','Entered a '+str(building)+' and lost '+str(buildingsList[i][1])+' gold...Ouch.. ' + str(timestamp)])
				request.session.modified = True
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')