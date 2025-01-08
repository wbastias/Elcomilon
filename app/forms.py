from django import forms
from . import models
# importando el formulario para el registro en models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from app import validators
from django.forms import ValidationError


class ContactForm(forms.ModelForm):
    # nombre = forms.CharField(widget=forms.TextInput(
    # attrs={"class": "form-control"}))

    class Meta:
        model = models.Contacto
        # fields = "nombre", "correo", "tipo_consulta", "mensaje", "aviso" estes es para darle el orden que yo quiero

        fields = '__all__'
        # esto es para importar todo lo que ya esta en models realizado en contacto


# se llamara el formulario que se encuentra en models para poder mostrarlo en la pagina


class ProductForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1000, max_value=1000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = models.Product.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya Existe")
        return nombre

    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2", ]
        

