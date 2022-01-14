from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('name', 'id')
    sort_values = {
        'name': 'name',
        'min_price': '-price',
        'max_price': 'price',
        'id': 'id',
    }
    phones = Phone.objects.order_by(sort_values[sort]).all()
    template = 'catalog.html'
    context = {'phones': phones,
               'sort': sort, }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).get()
    context = {'phone': phone, }
    return render(request, template, context)
