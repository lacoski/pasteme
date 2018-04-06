from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={               
            'class': 'form-control',
            'placeholder': 'User name',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={               
            'class': 'form-control',
            'placeholder': 'Password',
        }
    ))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password= password)
        if not user:
            raise forms.ValidationError("This is User does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")
        if not user.is_active:
            raise forms.ValidationError("This user is not longer active")       
        return super(UserLoginForm, self).clean(*args, **kwargs)