from django.shortcuts import render
from .models import *
# Create your views here.


def Store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/Store.html', context)


def Cart(request):
    return render(request, 'store/Cart.html')


def Checkout(request):
    return render(request, 'store/Checkout.html')


