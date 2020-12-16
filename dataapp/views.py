from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
	return HttpResponse("This will be the homepage view")
# Create your views here.
