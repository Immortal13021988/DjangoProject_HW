from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseGone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product


# def prod_list(request):
#     prods = Product.objects.all()
#     context = {"prods": prods}
#     return render(request, "catalog/prod_list.html", context)

class ProductDetailView(DetailView):
    model = Product

# def prod_detail(request, pk):
#     prod = get_object_or_404(Product, pk=pk)
#     context = {"prod": prod}
#     return render(request, "catalog/prod_detail.html", context)


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:prod_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:prod_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    # from django.contrib import messages
    #
    # class MyFormView(FormView):
    #     # твои настройки
    #
    #     def form_valid(self, form):
    #         messages.success(self.request, "Форма успешно отправлена!")
    #         return super().form_valid(form)

# def contacts(request):
#     if request.method == "POST":
#         return HttpResponseGone("Данные успешно получены!")
#     return render(request, "catalog/contacts.html")
