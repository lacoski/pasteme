from rest_framework.serializers import ModelSerializer                    
from rest_framework import serializers

from userzone.models import Paste

class PasteCreateSerializer(ModelSerializer):    
    class Meta:
        model = Paste
        fields = [
            #'id',
            'paste_name', 
            'type_content_paste',
            'content_paste', 
            #'short_link'
        ]    

class PasteDetailSerializer(ModelSerializer):
    class Meta:
        model = Paste
        fields = [
            'id',
            'paste_name', 
            'type_content_paste', 
            'content_paste', 
            'short_link'
        ]


class PasteListSerializer(ModelSerializer):
    class Meta:
        model = Paste
        fields = [            
            'paste_name', 
            'type_content_paste', 
            'content_paste', 
            'short_link'
        ]
