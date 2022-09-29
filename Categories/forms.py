from socket import fromshare
from attr import fields
from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"
        exclude=["slug"]


class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields="__all__"
        exclude=["slug","category"]



