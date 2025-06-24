# forms.py
from django import forms
from .models import Product,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
      }