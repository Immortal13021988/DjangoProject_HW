from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_list_from_cache():
    """Получение списка продуктов из кеша, если кеш отсутствует, получение списка из базы данных с записью в кеш"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "prod_list"
    prod_list = cache.get(key)
    if prod_list is not None:
        return prod_list
    prod_list = Product.objects.all()
    cache.set(key, prod_list)
    return prod_list


def get_products_by_category(category):
    """Функция получения списка продуктов по категории"""
    return Product.objects.filter(category=category)



