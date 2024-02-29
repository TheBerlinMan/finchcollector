from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Stuff, Things
from .forms import WalkingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stuff_index(request):
  stuff = Stuff.objects.all()
  return render(request, 'stuff/index.html', {'stuff': stuff })

def stuff_detail(request, stuff_id):
  stuff = Stuff.objects.get(id=stuff_id)
  walking_form = WalkingForm()
  return render(request, 'stuff/detail.html', {
    'stuff': stuff, 'walking_form': walking_form
  })

class StuffCreate(CreateView):
  model = Stuff
  fields = '__all__'
  success_url='/stuff/'

class StuffUpdate(UpdateView):
  model = Stuff
  fields = ['description', 'type', 'size', 'age']

class StuffDelete(DeleteView):
  model = Stuff
  success_url='/stuff/'

def add_walk(request, stuff_id):
  form = WalkingForm(request.POST)
  if form.is_valid():
    new_walk = form.save(commit=False)
    new_walk.stuff_id = stuff_id
    new_walk.save()
  return redirect('stuff-detail', stuff_id = stuff_id)

class ThingsCreate(CreateView):
  model = Things
  fields = '__all__'

class ThingsList(ListView):
  model = Things

class ThingsDetail(DetailView):
  model = Things