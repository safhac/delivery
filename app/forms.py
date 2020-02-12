from django.forms import ModelForm
from app.models import *



class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
        