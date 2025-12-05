from django.urls import path

from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="prod_list"),
    path("contacts/", ContactTemplateView.as_view(extra_context={"header": "О сайте"}), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="prod_detail"),
    path("product/create", ProductCreateView.as_view(), name="prod_create"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(), name="prod_update"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="prod_delete"),
]
