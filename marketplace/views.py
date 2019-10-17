from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import  AuthenticationForm
from .models import Producto, Oferta

 
#vista al home
def home_view(request):
    return render(request,'home.html')

#registrarse
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            #login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def create_prod(request):
        if request.method == 'POST':
                form = ProductoForm(request.POST, request.FILES)
                if form.is_valid():
                        prod = form.save()
                        return redirect('producto')
        else:
                form = ProductoForm()
        return render(request, 'producto/create.html', {'form': form})

#iniciar sesion
def login_view(request):
        if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
                if form.is_valid():
                        user = form.get_user()
                        login(request, user)
                        return redirect('home')
        else:
                form = AuthenticationForm()
        return render(request,'user/login.html',{'form':form})


#Todos los libros, vista basada en funcion

def Productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/products.html', {'productos': productos})


def Ofertas(request):
        return render(request,'producto/ofertas.html')

def profile_view(request):
        return render(request, 'user/profile.html')