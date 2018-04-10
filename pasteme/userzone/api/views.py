from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from userzone.helper import FileIO
from userzone.models import Paste
from .serializers import (
    PasteListSerializer, 
    PasteDetailSerializer,
    PasteCreateSerializer
)

class PasteCreateAPIView(CreateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteCreateSerializer    
    
    def perform_create(self, serializer):        
        content = serializer.validated_data['content_paste']
        serializer.save(
            user_own=self.request.user,
            content_paste='none'
            )
        # target = Paste.objects.get(id=obj.id)     
        # FileIO.writeToFile(content, target.short_link)    
        content = serializer.validated_data['short_link']    
        print(content)

class PasteDetailAPIView(RetrieveAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteDetailSerializer
    lookup_field = 'short_link'

class PasteUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteDetailSerializer
    lookup_field = 'short_link'

class PasteDeleteAPIView(DestroyAPIView):
    queryset = Paste.objects.all() 
    serializer_class = PasteDetailSerializer
    lookup_field = 'short_link'


class PasteListAPIView(ListAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteListSerializer
    
