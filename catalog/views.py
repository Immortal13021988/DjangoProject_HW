from django.shortcuts import render
from django.http import HttpResponseGone

# Create your views here.


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == "POST":
        return HttpResponseGone("Данные успешно получены!")
    return render(request, "catalog/contacts.html")
