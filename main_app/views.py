from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stuff, Things
from .forms import WalkingForm

# def home(request):
#   return render(request, 'home.html')
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def stuff_index(request):
  stuff = Stuff.objects.filter(user=request.user)
  return render(request, 'stuff/index.html', {'stuff': stuff })

@login_required
def stuff_detail(request, stuff_id):
  stuff = Stuff.objects.get(id=stuff_id)
  things_stuff_doesnt_have = Things.objects.exclude(id__in = stuff.things.all().values_list('id'))
  walking_form = WalkingForm()
  return render(request, 'stuff/detail.html', {
    'stuff': stuff, 
    'walking_form': walking_form,
    'things': things_stuff_doesnt_have
  })

class StuffCreate(LoginRequiredMixin, CreateView):
  model = Stuff
  fields = ['description', 'type', 'size', 'age']
  success_url='/stuff/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class StuffUpdate(LoginRequiredMixin, UpdateView):
  model = Stuff
  fields = ['description', 'type', 'size', 'age']

class StuffDelete(LoginRequiredMixin, DeleteView):
  model = Stuff
  success_url='/stuff/'

@login_required
def add_walk(request, stuff_id):
  form = WalkingForm(request.POST)
  if form.is_valid():
    new_walk = form.save(commit=False)
    new_walk.stuff_id = stuff_id
    new_walk.save()
  return redirect('stuff-detail', stuff_id = stuff_id)

class ThingsCreate(LoginRequiredMixin, CreateView):
  model = Things
  fields = '__all__'

class ThingsList(LoginRequiredMixin, ListView):
  model = Things

class ThingsDetail(LoginRequiredMixin, DetailView):
  model = Things

class ThingsUpdate(LoginRequiredMixin, UpdateView):
  model = Things
  fields = ['name', 'color']

class ThingsDelete(LoginRequiredMixin, DeleteView):
  model = Things
  success_url = '/things/'

@login_required
def assoc_things(request, stuff_id, things_id):
  Stuff.objects.get(id=stuff_id).things.add(things_id)
  return redirect('stuff-detail', stuff_id=stuff_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)