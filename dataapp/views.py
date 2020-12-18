from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
	return render(request, 'dataapp/homepage.html')
# Create your views here.
