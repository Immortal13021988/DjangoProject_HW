from django import forms
from django.forms import BooleanField

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content", "photo", "is_published")

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for fild_name, fild in self.fields.items():  # этот вариант, что бы побыстрому сделать нормальночитаемые формы
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"

        self.fields["title"].widget.attrs.update({
            "placeholder": "Введите заголовок"
        })
        self.fields["content"].widget.attrs.update({
            "placeholder": "Введите основной текст"
        })



