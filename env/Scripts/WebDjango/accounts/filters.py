from pyexpat import model
from django.urls import clear_script_prefix
import django_filters

from .models import *

class OrderFilter(django_filters.filterset):
    class Meta():
        model = Order
        fields = "__all__"