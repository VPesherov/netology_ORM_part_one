from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    servings = request.GET.get("sort", 'name')
    filters = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    filter = filters.get(servings)
    template = 'catalog.html'
    phone_objects = Phone.objects.filter().order_by(filter)
    # phones = []  # [{},{},{},...]
    phones = [{'name': p.name, 'image': p.image, 'slug': p.slug, 'price': p.price} for p in phone_objects]
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    for p in phone_object:
        phone = {
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'release_date': p.release_date,
            'lte_exists': p.lte_exists
        }
    context = {'phone': phone}
    return render(request, template, context)
