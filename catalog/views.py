from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseGone

from catalog.models import Product
# Create your views here.


def prod_list(request):
    prods = Product.objects.all()
    context = {"prods": prods}
    return render(request, "catalog/prod_list.html", context)


def contacts(request):
    if request.method == "POST":
        return HttpResponseGone("Данные успешно получены!")
    return render(request, "catalog/contacts.html")


def prod_detail(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {"prod": prod}
    return render(request, "catalog/prod_detail.html", context)
