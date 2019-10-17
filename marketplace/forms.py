from django.contrib.auth.forms import UserCreationForm, forms
from .models import User, Producto

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'descripcion', 'imagen', 'proveedor', 'precio')