from django.views.generic import UpdateView
from .models import Car,Category,Manufacturer
from .forms import SearchCarForm, AddCarForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

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


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    related_cars = Car.objects.filter(category=car.category).exclude(id=car.id)[:5]

    context = {'car':car,
               'related_cars':related_cars}
    return render(request, 'shop/car_detail.html', context)

    

@login_required
def car_form_view(request, car_id=None):
    if car_id:
        car =get_object_or_404(Car,id=car_id)
    else:
        car = None
    
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('shop:car_detail', car_id=car.id)
    else:
        form = AddCarForm(instance=car)

    context = {
        'form':form,
        'car':car

    }
    return render(request, 'shop/add_cars.html', context)

@login_required
def remove_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return redirect('shop:home')