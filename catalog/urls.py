from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.prod_list, name="prod_list"),
    path("contacts/", views.contacts, name="contacts"),
    path("prod/<int:pk>", views.prod_detail, name="prod_detail"),
]
