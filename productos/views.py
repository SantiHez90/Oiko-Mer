from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from productos.models import productos,categoria_Intermedia,categorias
# Create your views here.

def productos(request):
    categorias_list = categorias.objects.all()
    
    return render(request, 'productos.html', {'categorias_list': categorias_list})

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
            return render(request,'carrito.html',{'fname' : fname})
            
        else:
            messages.error(request, "Credenciales incorrectas")
            return redirect('signin')
    return render(request,"signin.html")