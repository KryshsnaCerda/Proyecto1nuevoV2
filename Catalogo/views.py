from django.shortcuts import render
from .models import cliente, Genero
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@login_required
def principal(request):
    context={}
    return render(request, 'Catalogo/principal.html', context)


def inicio(request):
    context={}
    return render(request, 'Catalogo/inicio.html', context)

@login_required
def catalogo(request):
    context={}
    return render(request, 'Catalogo/catalogo.html', context)

@login_required
def suscripcion(request):
    context={}
    return render(request, 'Catalogo/suscripcion.html', context)

@login_required
def login(request):
    context={}
    return render(request, 'Catalogo/login.html', context)

@login_required
def registrarse(request):
    context={}
    return render(request, 'Catalogo/registrarse.html', context)

def registrarse(request):
    if request.method != "POST":
        context={'mensaje':'registrado con exito'}
        return render(request, 'registrarse.html', context)
    
    else:
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']

        obj = User.objects.create_user( 
                                      username = nombre,
                                      password = contraseña,)
        obj.save()
        context={'mensaje':'registrado con exito'}
        return render(request, 'registrarse.html', context)
    
def menu(request):
    request.session["usuario"]="kcerda"
    usuario=request.session["usuario"]
    context ={'usuario':usuario}
    return render(request, 'principal.html', context)

@staff_member_required
def admin(request):
    admin = cliente.objects.all()
    context={'admin': admin}
    return render(request, 'admin.html', context) 