from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html', {'title' : 'Home - Django - Desenvolvimento WEB com Python'})

def contact(request):
	return render(request, 'contact.html', {'title' : 'Entre em contato - Django - Desenvolvimento WEB com Python'})