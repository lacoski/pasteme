from django import forms
from .models import Paste, Role, User


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class PasteForm(forms.ModelForm):    
    class Meta:
        model = Paste
        fields = ['paste_name', 'type_content_paste','content_paste', 'user_own', 'short_link']