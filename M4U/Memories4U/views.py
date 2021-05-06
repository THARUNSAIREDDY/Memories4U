from django.shortcuts import render,redirect
from M4U import settings
from .models import Events,Gallary
# Create your views here.

def home(request):

	dest=Events.objects.all()
	return render(request,'html/home.html',{"dest":dest})

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')


def gallary(request):

	photo=Gallary.objects.all()

	return render(request,'html/gallary.html',{"photo":photo})

def events(request):
	dest=Events.objects.all()
	return render(request,'html/events.html',{"dest":dest})





