import django_filters as filters #custom library
from django_filters import DateFilter as date_filter #custom library
from .models import *

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
        exclude = ['customer', 'date_created']        


class OrderFilter(filters.FilterSet):
    # start_date = date_filter(field_name='date_created', lookup_expr='gte')
    # end_date = date_filter(field_name='date_created', lookup_expr='lte')
    class Meta:
        model = Order
        fields = ['status']
        

class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
        


