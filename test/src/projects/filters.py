import django_filters
from .models import *
from django_filters import CharFilter

class ItemFilter(django_filters.FilterSet):
    class Meta:
        item_title = CharFilter(field_name='item_title',lookup_expr='icontains')
        model = Listing_Database
        fields = [ 'item_title','item_category','county']
