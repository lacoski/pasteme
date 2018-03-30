from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Paste

# Create your views here.

def index(request):
    list_paste = Paste.objects.all()
    context = {
        'title': 'List created paste',
        'sub_title':'lets share your code ',
        'list_paste': list_paste,
    }
    return render(request, 'userzone/index.html', context)


def create_paste(request):
    context = {
        'create_paste_title': 'Create new paste',
        'create_paste_sub_title':'lets share your code ',
    }
    return render(request, 'userzone/create_paste.html', context)

#class CreatePasteView():
