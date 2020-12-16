from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
	return HttpResponse("This will be the homepage")
# Create your views here.
