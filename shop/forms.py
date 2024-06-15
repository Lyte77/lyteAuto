from django import forms
from .models import Category, Manufacturer, Car

class SearchCarForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search for your dream car')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all(),required=False)


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['category', 'name','manufacturer', 'description','price']