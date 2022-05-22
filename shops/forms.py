from django import forms
from django.forms.models import modelformset_factory
from .models import Variation, ProductFeatured

class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields  = [
            'product',
            'name',
            'price',
            'sale_price',
            'color',
            'inventory',
            'image',
            'active',
            'currency'
        ]

class ProductFeaturedForm(forms.ModelForm):
    class Meta:
        model = ProductFeatured
        fields  = [
            'product',
            'name',
            'text',
            'active',
        ]



