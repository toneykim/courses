# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from . models import Course

# Create your views here.
def index(request):

	query = Course.objects.all()
	context = {
	"query" : query


	}




	return render(request, 'Course/index.html', context)


def process(request):
	if request.method == "POST":
		Course.objects.create(
			course_name=request.POST['name'],
			description=request.POST['description']
			)

	return redirect('/')


def remove(request, number):

	query = Course.objects.filter(id=number)

	context = {

	"query" : query

	}
	



	return render(request, 'Course/remove.html', context)


def remove2(request):
	if request.method == "POST":
		number = request.POST['yes']


		Course.objects.filter(id = number).delete()

	return redirect('/')