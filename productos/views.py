from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from productos.models import productos,categoria_Intermedia,categorias
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

def categoria(request):
    
    categorias_list = categorias.objects.all()
    return render(request, 'categoria.html', {'categorias_list': categorias_list})

def categoria_intermedia(request, categoria_id):
    categoria = categorias.objects.get(id=categoria_id)
    categoria_intermedia_list = categoria_Intermedia.objects.filter(categoria=categoria)
    return render(request, 'categoria_intermedia.html', {'categoria_intermedia_list': categoria_intermedia_list})

def productos_categoria_intermedia(request, categoria_intermedia_id):
    categoria_intermedia = categoria_Intermedia.objects.get(id=categoria_intermedia_id)
    productos_list = productos.objects.filter(categoria_Intermedia=categoria_intermedia).order_by('intprecio')
    labels = []
    data = []

    for producto in productos_list:
        labels.append(producto.nomMarca)
        data.append(producto.intprecio)

    data = [float(d) for d in data] 
    context = {
    'productos_list': productos_list,
    'labels': json.dumps(labels),  # Convertir a cadena JSON para pasarlo al JavaScript
    'data': json.dumps(data),  # Convertir a cadena JSON para pasarlo al JavaScript
}
    return render(request, 'productos_categoria_intermedia.html', context)



def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']   

            if pass1 != pass2:
                return HttpResponse("Las contraseñas no coinciden")
            else:
                myuser = User.objects.create_user(username,email,pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save
                messages.success(request, "Tu cuenta ha sido creada exitosamente")
                return render(request,'signup.html')
    
def carrito(request):
    return render(request,'carrito.html')
    


def home(request):
    return render(request,'home.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
        if request.method == 'GET':
            return render(request,'signin.html')
        else:
            if request.method =='POST':
                username = request.POST['username']
                pass1 = request.POST['pass1']
                user = authenticate(username=username, password=pass1)
            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request,'home.html',{'fname' : fname})
            else:
                messages.error(request, "Credenciales incorrectas")
                return redirect('home')