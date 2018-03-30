from django.urls import path

from . import views

urlpatterns = [
    # ex: /userzone/
    path('', views.index, name='index'),

    path('createpaste/', views.create_paste),
]
