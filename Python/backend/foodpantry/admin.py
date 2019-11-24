from django.contrib import admin
from .models import PantryItem
  
# Register your models here.
admin.site.site_header = 'Food Pantry Administration'

admin.site.register(PantryItem)
