from django.shortcuts import render
from .forms import UsRegForm
def home(request):
	return render(request,'html/home.html')
def usregister(request):
	t=UsRegForm()
	return render(request,'html/register.html',{"p":t})
