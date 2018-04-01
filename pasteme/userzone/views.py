from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Paste
from .forms import NameForm,PasteForm
# Create your views here.

def index(request):
    list_paste = Paste.objects.all()
    context = {
        'title': 'List created paste',
        'sub_title':'lets share your code ',
        'list_paste': list_paste,
    }
    return render(request, 'userzone/index.html', context)


"""
def create_paste(request):
    context = {
        'create_paste_title': 'Create new paste',
        'create_paste_sub_title':'lets share your code ',
    }
    return render(request, 'userzone/create_paste.html', context)
"""

def get_name(request):     
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/userzone/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'userzone/name.html', {'form': form})

def thanks(request):
    context = {
        'create_paste_title': 'Create new paste',
        'create_paste_sub_title':'lets share your code ',
    }
    return render(request, 'userzone/thanks.html', context)


def get_detail_paste(request, paste_name, paste_id):
    context = {
        'paste_name': paste_name,
        'paste_id': paste_id
    }
    return render(request, 'userzone/get_detail_paste.html', context)


def list_paste(request):
    Pastes = Paste.objects.all()
    return render(request, 'userzone/pastes.html',{'Pastes':Pastes})

def create_paste(request):
    form = PasteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_pastes')

    return render(request, 'userzone/pastes-form.html', {'form': form})

def update_paste(request,id):
    Paste_ = Paste.objects.get(id=id)
    form = PasteForm(request.POST or None, instance=Paste_)

    if form.is_valid():
        form.save()
        return redirect('list_paste')
    return render(request, 'userzone/pastes-form.html', {'form': form, 'paste': Paste_})

def delete_paste(request,id):
    Paste_ = Paste.objects.get(id=id)
    if request.method == 'POST':
        Paste_.delete()
        return redirect('list_pastes')
    
    return render(request, 'userzone/pastes-delete-confirm.html', {'paste': Paste_})