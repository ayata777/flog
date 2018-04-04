from django import forms
from .models import Category,Specify,BigCategory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class BigCategoryForm(forms.ModelForm):

    class Meta:
        model = BigCategory
        fields = ('categories',)
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('categories',)
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

 
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
class SpecifyForm(forms.ModelForm):

    class Meta:
        model = Specify
        fields = ('title','image',)

