from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet
 
# Register your models here.
admin.site.site_header = 'Food Pantry Admin'

class PantryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Snippet, PantryAdmin)
admin.site.unregister(Group)