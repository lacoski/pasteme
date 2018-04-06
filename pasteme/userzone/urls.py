from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.list_paste_template, name = 'list_paste_template'),
    path('create_paste', views.create_paste_template, name = 'create_paste_template'),    
    path('update_paste/<int:id>', views.update_paste_template, name = 'update_paste_template'),
    path('delete_paste/<int:id>', views.delete_paste_template, name = 'delete_paste_template'),
    path('review_paste/<slug:id>', views.review_paste_template, name = 'review_paste_template'),
    path('search_paste/', views.search_paste_template, name = 'search_paste_template'),
]
