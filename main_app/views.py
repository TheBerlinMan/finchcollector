from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Stuff

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stuff_index(request):
  stuff = Stuff.objects.all()
  return render(request, 'stuff/index.html', {'stuff': stuff })

def stuff_detail(request, stuff_id):
  stuff = Stuff.objects.get(id=stuff_id)
  return render(request, 'stuff/detail.html', { 'stuff': stuff })

class StuffCreate(CreateView):
  model = Stuff
  fields = '__all__'
