from django.contrib import admin
from .models import Stuff, Walking, Things

# Register your models here.
admin.site.register(Stuff)
admin.site.register(Walking)
admin.site.register(Things)