from .models import Listing_Database
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# class to allow user update their own data
class CreatingListingForm(forms.ModelForm):
    class Meta:
        model = Listing_Database
        fields = ['item_title','item_category','description','price','county','phone_number' ,'image']
        