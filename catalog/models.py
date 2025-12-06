from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование",
        # help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание",
        # help_text="Заполните описание"
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        # help_text="Загрузите фото",
        # blank разрешает быть пустым на странице, null в базе данных
    )
    category = models.ForeignKey(  # связывает две таблицы через название категории
        "Category",  # можно писать без кавычек, тогда надо что бы Category была выше Products
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        # help_text="Выберите категорию",
        related_name="products",
    )
    price = models.FloatField(
        blank=True, null=True, verbose_name="Цена",
        # help_text="Введите цену"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # заполняет дату при добавлении и больше не меняет
    updated_at = models.DateTimeField(
        auto_now=True
    )  # меняет дату каждый раз при изменении

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Заполните описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]
