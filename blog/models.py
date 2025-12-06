from django.db import models


class Blog(models.Model):
    STATUS_CHOICES = (
        (" draft", "Черновик"),
        (" published", "Опубликовано"),
    )
    title = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Заполните содержимое"
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        # blank разрешает быть пустым на странице, null в базе данных
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # заполняет дату при добавлении и больше не меняет
    updated_at = models.DateTimeField(
        auto_now=True
    )  # меняет дату каждый раз при изменении
    is_published = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = [
            "title",
        ]
