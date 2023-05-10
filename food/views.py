from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, "food/index.html", context)


def detail(request, item_id):
    item = Item.objects.get(pk= item_id)
    context = {
        'item': item,
    }
    return render(request, "food/detail.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    context = {
        'form': form,
    }

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'food/item-form.html', context)

def update_item(request,id):
    item = Item.objects.get(id= id)
    form = ItemForm(request.POST or None, instance= item)

    context = {
        'form': form,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'food/item-form.html', context)

def delete_item(request,id):
    item = Item.objects.get(id= id)

    context = {
        'item': item,
    }

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    
    return render(request, 'food/item-delete.html', context)
     