from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Stuff, Things
from .forms import WalkingForm

# def home(request):
#   return render(request, 'home.html')
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def stuff_index(request):
  stuff = Stuff.objects.all()
  return render(request, 'stuff/index.html', {'stuff': stuff })

def stuff_detail(request, stuff_id):
  stuff = Stuff.objects.get(id=stuff_id)
  things_stuff_doesnt_have = Things.objects.exclude(id__in = stuff.things.all().values_list('id'))
  walking_form = WalkingForm()
  return render(request, 'stuff/detail.html', {
    'stuff': stuff, 
    'walking_form': walking_form,
    'things': things_stuff_doesnt_have
  })

class StuffCreate(CreateView):
  model = Stuff
  fields = ['description', 'type', 'size', 'age']
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

class ThingsUpdate(UpdateView):
  model = Things
  fields = ['name', 'color']

class ThingsDelete(DeleteView):
  model = Things
  success_url = '/things/'

def assoc_things(request, stuff_id, things_id):
  Stuff.objects.get(id=stuff_id).things.add(things_id)
  return redirect('stuff-detail', stuff_id=stuff_id)

