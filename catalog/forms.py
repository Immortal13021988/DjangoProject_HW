from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField


from .models import Product

STOP_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "photo", "category", "price")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for fild_name, fild in self.fields.items():  # этот вариант, что бы побыстрому сделать нормальночитаемые формы
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"

        self.fields["name"].widget.attrs.update({
            "placeholder": "Введите название"
        })
        self.fields["description"].widget.attrs.update({
            "placeholder": "Введите описание"
        })
        self.fields["price"].widget.attrs.update({
            "placeholder": "Введите цену"
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise ValidationError('Цена не может быть отрицательной. Введите другое значение.')
        return price

    # def clean_photo(self):
    #     photo = self.cleaned_data.get('photo')
    #     if photo:
    #         if photo.file.content_type not in ['photo/jpeg', 'photo/png']:
    #             raise ValidationError('Формат изображения должен быть JPEG или PNG.')
    #         if photo.size > 5 * 1024 * 1024:
    #             raise ValidationError('Размер изображения не должен превышать 5 МБ.')
    #     return photo

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     description = cleaned_data.get("description")
    #     for word in STOP_WORDS:
    #         if name and description and word in name.lower():
    #             self.add_error("name", f"Название не может содержать слово: {word.upper()}")
    #         elif name and description and word in description.lower():
    #             self.add_error("description", f"Название не может содержать слово: {word.upper()}")

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in STOP_WORDS:
            if name and word in name.lower():
                self.add_error("name", f"Название не может содержать слово: {word.upper()}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in STOP_WORDS:
            if description and word in description.lower():
                self.add_error("description", f"Название не может содержать слово: {word.upper()}")
        return description
