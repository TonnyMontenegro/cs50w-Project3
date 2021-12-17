from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect, request
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

contador = Cuenta_func.objects.first()
#creacion de el objeto user con super usuario
superuser = User.objects.filter(is_superuser=True)
if contador is None:
    n_contador =Cuenta_func(cuenta_numero=1)
    n_contador.save()
if superuser.count() == 0:
    superuser=User.objects.create_user("Admin","Admin@pizzapp.com","Password")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()

def index(request):
    if not request.user.is_authenticated:
        return redirect("register")
    else: return redirect("home")

@csrf_protect
def register_view(request):
    if not request.user.is_authenticated:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,'Cuenta registrada bajo el nombre de usuario de: '+ user)
                return redirect('login')
        context= {'form':form}
        return render(request, 'register.html',context)
    else: return redirect("home")

@login_required(login_url="login")
def menu_view(request):
    exist = orden.objects.filter(usuario=request.user,tipo="Carrito").exists()
    if exist:
        print("URL add: Orden de carrito ya existente")
    else:
        orden.objects.create(usuario=request.user,tipo="Carrito")
    context = {
        "RegularPizzas": Pizza.objects.filter(tipo='Regular'),
        "SicilianPizzas": Pizza.objects.filter(tipo='Sicilian'),
        "Ensaladas": Ensalda.objects.all,
        "Toppings": Topping.objects.all,
        "Subs": sub.objects.all,
        "Pastas": Pasta.objects.all,
        "Cenas": Cena.objects.all,
        "Extras": Extra.objects.all,
        "orden": orden.objects.get(usuario=request.user,tipo="Carrito")
    }
    return render(request,'menu.html',context)

@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Nombre de usuario o contraseña incorrecta')
        context = {}
        return render(request,"login.html",context)
    else: return redirect("home")

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def add(request,uid,categoria):
    ordenx =  orden.objects.get(usuario=request.user,tipo="Carrito")
    if categoria == "Pizza":    
        elemento = Pizza.objects.get(uid=uid)
        if request.POST.get("Toppings") is not None:
            toppingslist=[]
            for topping in request.POST.getlist("Toppings"):
                toppinginst = models.Topping.objects.get(uid=int(topping))
                toppingslist.append(toppinginst)
            carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx,tipo_pizza=elemento.tipo)
            carrito_item.toppingPizza.add(*toppingslist)
            carrito_item.save()
        else:
            carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx,tipo_pizza=elemento.tipo)
    elif categoria == "Salad":
        elemento = models.Ensalda.objects.get(uid=uid)
        carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx)
    elif categoria == "Sub":
        elemento = models.sub.objects.get(uid=uid)
        extrasprice = 0

        if request.POST.get("Extras") is not None:
            extrasList=[]
            for extraitem in request.POST.getlist("Extras"):
                extrainst = models.Extra.objects.get(uid=int(extraitem))
                extrasList.append(extrainst)
                extrasprice += extrainst.precio
            carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,monto_extras=extrasprice,orden=ordenx)
            carrito_item.extras_name.add(*extrasList)
            carrito_item.save()
        else:
            carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx)

    elif categoria == "Pasta":
        elemento = models.Pasta.objects.get(uid=uid)
        carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx)


    elif categoria == "Cena":
        elemento = models.Cena.objects.get(uid=uid)
        carrito_item= CarritoItem.objects.create(usuario=request.user,elemento=elemento,precio=elemento.precio,orden=ordenx)
    messages.info(request,"Producto añadido al carrito")
    return redirect("home")

@login_required(login_url="login")
def cart(request):
    context={}
    ordenx = orden.objects.get(usuario=request.user,tipo="Carrito")
    context['orden'] = ordenx
    monto=0.0
    for item in CarritoItem.objects.filter(orden=ordenx):
        monto = monto + float(item.precio) + float(item.monto_extras)
    ordenx.monto = monto
    ordenx.save()
    context['items'] = CarritoItem.objects.filter(orden=ordenx).order_by()
    return render(request,"cart.html",context)

@login_required(login_url="login")
def delete_item(request,pk):
    CarritoItem.objects.filter(pk=pk).delete()
    messages.error(request,"Producto eliminado del carrito")
    return redirect('cart')

@login_required(login_url="login")
def make_order(request,pk):
    ordenx = orden.objects.get(usuario=request.user,tipo="Carrito",pk=pk)
    ordenx.tipo = "Orden"
    ordenx.estado = "En proceso"
    ordenx.save()
    messages.success(request,"Orden realizada")

    context={}
    context['orden'] = ordenx
    monto=0.0
    for item in CarritoItem.objects.filter(orden=ordenx):
        monto = monto + float(item.precio) + float(item.monto_extras)
    ordenx.monto = monto
    ordenx.save()
    context['items'] = CarritoItem.objects.filter(orden=ordenx).order_by()

    msg_plain = render_to_string('email.txt', context)
    msg_html = render_to_string('email.html',context)

    send_mail(
        'Confirmacion de orden',
        msg_plain,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        html_message=msg_html,
    )
    exist = orden.objects.filter(usuario=request.user,tipo="Carrito").exists()
    if exist:
        print("URL add: Orden de carrito ya existente")
    else:
        orden.objects.create(usuario=request.user,tipo="Carrito")
    return redirect('orders')

@login_required(login_url="login")
def orders(request):
    context = {}
    context["ordenes"] = orden.objects.filter(usuario=request.user,tipo="Orden").all().order_by("-fecha")
    context["ordenesAdmin"] = orden.objects.filter(tipo="Orden").all().order_by("-fecha")
    return render(request,"orders.html",context)

@login_required(login_url="login")
def state_change(request,state,pk):
    ordenx=orden.objects.get(pk=pk)
    context={}
    if state == "en_proceso":
        ordenx.estado = "En proceso"
        ordenx.save()
        context['orden']=ordenx
        email_estado = render_to_string('email_estado.txt', context)
        send_mail(
            'Estado de orden',
            email_estado,
            settings.EMAIL_HOST_USER,
            [ordenx.usuario.email],
        )
    elif state == "enviada":
        ordenx.estado = "Enviada"
        ordenx.save()
        context['orden']=ordenx
        email_estado = render_to_string('email_estado.txt', context)
        send_mail(
            'Estado de orden',
            email_estado,
            settings.EMAIL_HOST_USER,
            [ordenx.usuario.email],
        )
    elif state == "recibida":
        ordenx.estado = "Recibida"
        ordenx.save()
        send_mail(
        'Estado de orden',
        'hola esperamos estes satisfech@ con tu orden, muchas gracias por preferirnos.',
        settings.EMAIL_HOST_USER,
        [ordenx.usuario.email],
        )
    
    messages.success(request,"Estado de orden actualizado con exito")
    return redirect('orders')

@login_required(login_url="login")
def order(request,pk):
    context={}
    if request.user.is_staff:
        ordenx = orden.objects.get(pk=pk)
        context['orden'] = ordenx
        monto=0.0
        for item in CarritoItem.objects.filter(orden=ordenx):
            monto = monto + float(item.precio) + float(item.monto_extras)
        ordenx.monto = monto
        ordenx.save()
        context['items'] = CarritoItem.objects.filter(orden=ordenx)
    else:
        ordenxstate = orden.objects.filter(pk=pk,usuario=request.user).exists()
        if ordenxstate:
            ordenx = orden.objects.get(pk=pk,usuario=request.user)
            context['orden'] = ordenx
            monto=0.0
            for item in CarritoItem.objects.filter(orden=ordenx):
                monto = monto + float(item.precio) + float(item.monto_extras)
            ordenx.monto = monto
            ordenx.save()
            context['items'] = CarritoItem.objects.filter(orden=ordenx)
        else:
            messages.error(request,"No tienes acceso a cuentas que no son tuyas")
            return redirect("orders")
    return render(request,"order.html",context)