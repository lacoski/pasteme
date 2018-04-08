from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.views import generic
from .models import Paste
from .forms import PasteCreateForm,PasteFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
# Create your views here.

NUMBER_ITEM_PER_PAGE = 5
SUPPORT_LANGUAGE = ['Apache', 'Bash', 'C#', 'C++', 'CSS', 'CoffeeScript', 'Diff', 'HTML', 'XML', 'HTTP', 'Ini',  
                    'JSON', 'Java', 'JavaScript', 'Makefile', 'Markdown', 'Nginx', 'Objective-C', 'PHP', 'Perl',  
                    'Python', 'Ruby', 'SQL', 'Shell Session'] 

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
    list_syntax = SUPPORT_LANGUAGE
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
    list_syntax = SUPPORT_LANGUAGE
    form = PasteCreateForm(request.POST or None, instance=Paste_)

    if form.is_valid():
        form.save()        
        return redirect('review_paste_template', id=Paste_.short_link)
    return render(request, 'userzone/paste_create.html', {'form': form, 'paste': Paste_, 'title':'Update Paste' ,
                                                        'sub_title':'Changing your code','list_syntax':list_syntax})

def delete_paste_template(request,id):
    Paste_ = Paste.objects.get(id=id)
    if request.method == 'POST':
        Paste_.delete()
        return redirect('list_paste_template')
    
    return render(request, 'userzone/paste_delete.html', {'paste': Paste_, 'title':'Delete Paste' ,'sub_title':'Remote your code'})

def review_paste_template(request,id):
    Paste_ = Paste.objects.get(short_link=id)    
    return render(request, 'userzone/paste_review.html', {'paste': Paste_, 'title':'Review Paste' ,'sub_title':'See your code'})

def create_paste_guest_template(request):
    form = PasteCreateForm(request.POST or None)
    list_syntax = SUPPORT_LANGUAGE
    if form.is_valid():        
        obj = form.save(commit=False)         
        obj.save()
        target = Paste.objects.get(id=obj.id)        
        get_file = os.path.join(settings.MEDIA_ROOT, target.short_link)
        file = open(get_file,'w')
        content = request.POST.get('content_paste')
        file.write(content) 
        file.close()        
        return redirect('review_paste_guest_template', id=target.short_link)
    return render(request, 'userzone/paste_create_guest.html', {'form': form, 'title':'Create Paste', 
                                                                'sub_title':'Lets Sharing your code','list_syntax':list_syntax})

def review_paste_guest_template(request,id):
    Paste_ = Paste.objects.get(short_link=id)
    get_file = os.path.join(settings.MEDIA_ROOT, Paste_.short_link) 
    file = open(get_file,'r')
    content= file.read()
    file.close() 
    return render(request, 'userzone/paste_review_guest.html', {'paste': Paste_, 'title':'Review Paste' ,'sub_title':'See your code', 'content_paste':content})

def create_paste_file_guest_template(request):
    form = PasteFileForm(request.POST or None)
    list_syntax = SUPPORT_LANGUAGE
    if form.is_valid():        
        obj = form.save(commit=False)        
        #obj.save()
        #target = Paste.objects.get(id=obj.id)        
        #return redirect('review_paste_guest_template', id=target.short_link)
    return render(request, 'userzone/paste_create_guest.html', {'form': form, 'title':'Create Paste', 
                                                                'sub_title':'Lets Sharing your code','list_syntax':list_syntax})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'userzone/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'userzone/simple_upload.html')

def read_content_file(request):        
    get_file = os.path.join(settings.MEDIA_ROOT, 'README.md')
    #print(get_file)
    file = open(get_file, "r") 
    content= file.read()
    return render(request, 'userzone/review_upload_file.html',{
        'content':content,
    })

