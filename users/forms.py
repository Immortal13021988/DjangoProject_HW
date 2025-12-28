from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # phone_number = forms.CharField(
    #     max_length=15,
    #     help_text="Введите номер телефона",
    #     required=False)
    username = forms.CharField(max_length=15, required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            fild.widget.attrs["class"] = "form-control"

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
