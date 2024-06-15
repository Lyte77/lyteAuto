from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from shop.models import Car
from customers.models import Customer
from .models import Cart, CartItem

# Create your views here.

@login_required
def add_to_cart(request, id):
    car = get_object_or_404(Car, id=id)
    customer, created = Customer.objects.get_or_create(user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)

    cart_item , created = CartItem.objects.get_or_create(cart=cart,
                                                         car=car)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, id):
    customer = get_object_or_404(Customer, user=request.user)
    cart = get_object_or_404(Cart,customer=customer)
    cart_item = get_object_or_404(CartItem,cart=cart,id=id)
    cart_item.delete()
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    customer = get_object_or_404(Customer, user=request.user)
    cart = Cart.objects.get(customer=customer)
    cart_items = cart.items.all()
    total = sum(item.total_price() for item in cart_items)
  
    return render(request, 'cart/cart_detail.html',{
        'cart_items': cart_items,
        'total':total,
    })

@login_required
def update_cart(request,id):
    customer = get_object_or_404(Customer,user=request.user)
    cart = get_object_or_404(Cart, customer=customer)
    cart_item = get_object_or_404(CartItem, cart=cart, id=id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart:cart_detail')