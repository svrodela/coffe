from django.forms import ModelForm
from orders.models import OrderProduct

#filtra cada orden por usuario
class OrderProductForm(ModelForm):
    class Meta:
        model=OrderProduct
        fields=['product']