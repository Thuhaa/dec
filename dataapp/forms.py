from django import forms

class GetFileForm(forms.Form):
	file_path = forms.CharField(max_length=256)