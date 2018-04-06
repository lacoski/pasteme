from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.views import generic
from .models import Paste
from .forms import PasteCreateForm
# Create your views here.

NUMBER_ITEM_PER_PAGE = 5

def list_paste_template(request):
    Pastes = Paste.objects.filter(user_own=request.user.username)
    paginator = Paginator(Pastes, NUMBER_ITEM_PER_PAGE)
    page = request.GET.get('page')
    Pastes_with_paginator = paginator.get_page(page)
    return render(request, 'userzone/paste_lists.html',{'Pastes':Pastes_with_paginator,
                                                        'title':'Lists Paste' ,'sub_title':'All your code'} )

def search_paste_template(request):    
    search_text = request.GET.get('id')
    Pastes = Paste.objects.filter(user_own=request.user.username, paste_name__contains=search_text)    
    paginator = Paginator(Pastes, NUMBER_ITEM_PER_PAGE)
    page = request.GET.get('page')
    Pastes_with_paginator = paginator.get_page(page)
    return render(request, 'userzone/paste_lists.html',{'Pastes':Pastes_with_paginator, 'title':'Search Paste',
                                                        'sub_title':'Search your code','search_text':search_text,})

def create_paste_template(request):
    form = PasteCreateForm(request.POST or None)
    list_syntax = ['python','html']
    if form.is_valid():        
        obj = form.save(commit=False)
        #print(obj.content_paste )
        obj.user_own = request.user.username
        #print(obj.user_own)
        obj.save()
        target = Paste.objects.get(id=obj.id)        
        return redirect('review_paste_template', id=target.short_link)

    return render(request, 'userzone/paste_create.html', {'form': form, 'title':'Create Paste', 
                                                        'sub_title':'Lets Sharing your code','list_syntax':list_syntax})

def update_paste_template(request,id):
    Paste_ = Paste.objects.get(id=id)
    list_syntax = ['python','html']
    form = PasteCreateForm(request.POST or None, instance=Paste_)

    if form.is_valid():
        form.save()        
        return redirect('review_paste_template', id=Paste_.short_link)
    return render(request, 'userzone/paste_create.html', {'form': form, 'paste': Paste_, 'title':'Update Paste' ,'sub_title':'Changing your code','list_syntax':list_syntax})

def delete_paste_template(request,id):
    Paste_ = Paste.objects.get(id=id)
    if request.method == 'POST':
        Paste_.delete()
        return redirect('list_paste_template')
    
    return render(request, 'userzone/paste_delete.html', {'paste': Paste_, 'title':'Delete Paste' ,'sub_title':'Remote your code'})

def review_paste_template(request,id):
    Paste_ = Paste.objects.get(short_link=id)    
    return render(request, 'userzone/paste_review.html', {'paste': Paste_, 'title':'Review Paste' ,'sub_title':'See your code'})

