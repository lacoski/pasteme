from django.urls import path, re_path

from userzone.api.views import (
    PasteListAPIView,
    PasteDetailAPIView,
    PasteDeleteAPIView,
    PasteUpdateAPIView,
    PasteCreateAPIView
)

urlpatterns = [
    path('', PasteListAPIView.as_view(), name = 'list'),
    path('create/', PasteCreateAPIView.as_view(), name = 'create'),
    path('<slug:short_link>/', PasteDetailAPIView.as_view(), name = 'detail'),
    path('<slug:short_link>/edit/', PasteUpdateAPIView.as_view(), name = 'update'),
    path('<slug:short_link>/delete/', PasteDeleteAPIView.as_view(), name = 'delete'),
]
