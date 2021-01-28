from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
from .forms import GetFileForm


def homepageview(request):
	return render(request, 'dataapp/homepage.html')

def getfile_view(request):
	if request.method == "POST":
		form = GetFileForm(request.POST)
		if form.is_valid():
			file = form.cleaned_data['file_path']
			df = create_df(file)
			print(df)
			return HttpResponse(df)
	else:
		form = GetFileForm()
		return render(request, 'dataapp/upload.html', {'form':form})


def create_df(file):
	df = pd.read_csv(file)
	return df
