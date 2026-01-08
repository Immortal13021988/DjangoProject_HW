from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ProductForm, ProductModeratorForm, ProductOwnerModeratorForm
from .models import Product, Category
from .services import get_product_list_from_cache, get_products_by_category


class ProductUnpublishView(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if request.user.has_perm('catalog.can_unpublish_product'):
            product.is_published = False
            product.save()
            return redirect('catalog:products_list')
        else:
            return HttpResponseForbidden("У вас нет прав на выполнение этого действия.")


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = 'category_list'

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        print(get_products_by_category(category_id))
        return get_products_by_category(category_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.filter()
        return context

    #
    # def get_queryset(self):
    #     category_id = self.kwargs.get('id')
    #     print(category_id)
    #     return get_products_by_category(2)
    #


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.filter()
        return context

    def get_queryset(self):
        return get_product_list_from_cache()


# def prod_list(request):
#     prods = Product.objects.all()
#     context = {"prods": prods}
#     return render(request, "catalog/prod_list.html", context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


# def prod_detail(request, pk):
#     prod = get_object_or_404(Product, pk=pk)
#     context = {"prod": prod}
#     return render(request, "catalog/prod_detail.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def form_valid(self, form):
        prod = form.save()
        user = self.request.user
        prod.owner = user
        prod.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner and user.has_perm("catalog.can_unpublish_product"):
            return ProductOwnerModeratorForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm

        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.delete_product') and request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        # Логика исключения продукта
        product.delete()

        return redirect('catalog:product_list')


class ContactTemplateView(LoginRequiredMixin, TemplateView):
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
