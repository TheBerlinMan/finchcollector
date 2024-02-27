from django.shortcuts import render
from django.http import HttpResponse

class Stuff:
  def __init__(self, name, type, description, size):
    self.name = name
    self.type = type
    self.description = description
    self.size = size

stuff = [
  Stuff('Dingus', 'Water', 'A water dingus.', 'Large'),
  Stuff('Crank', 'Fire', 'Will make your pee smelly.', 'Small'),
  Stuff('Snoch', 'Air', 'Call for a good time.', 'Very Small'),
  Stuff('Horg', 'Earth', 'The Stuff of Life.', 'Super Big')
]

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')


def about(request):
  return render(request, 'about.html')

def stuff_index(request):
  return render(request, 'stuff/index.html', {'stuff': stuff })