from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

	
def password(request):
	charecters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length'))
	if request.GET.get('uppercase'):
		charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
		
	if request.GET.get('numbers'):
		charecters.extend(list('1234567890'))
		
	if request.GET.get('specialCharecters'):
		charecters.extend(list(r'~!@#$%^&*(_)'))
	genPassword = ''
	for i in range(length):
		genPassword += random.choice(charecters)
	return render(request, 'generator/password.html', {'Password': genPassword})
