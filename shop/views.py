from django.shortcuts import render
from .models import Car,Category,Manufacturer
from .forms import SearchCarForm

# Create your views here.
def home_view(request):
    cars = Car.objects.all()
    # query = request.GET.get('query')
    form = SearchCarForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        manufacturer = form.cleaned_data.get('manufacturer')

        if query:
            cars = cars.filter(name__icontains=query)
        if category:
            cars = cars.filter(category=category)
        if manufacturer:
            cars = cars.filter(manufacturer=manufacturer)



    context = {'cars':cars,
               'form':form}
    return render(request, 'shop/home.html', context)
