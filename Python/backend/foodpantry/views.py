from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PantryItem

# Create your views here.

def pantryView(request):
    all_items = PantryItem.objects.all()
    return render(request, 'main.html',
        {'items': all_items})

def addItem(request):
    new_item = PantryItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/foodpantry/') 

def deleteItem(request, item_id):
    item_to_delete = PantryItem.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/foodpantry/')

