from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to='users/avatar/',
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True, null=True
    )
    country = models.CharField(
        max_length=30,
        verbose_name="Страна",
        help_text="Введите страну",
        blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



