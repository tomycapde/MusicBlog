from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth import login, authenticate
from .models import Avatar


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            form2 = AuthenticationForm()
            return render(request,"login_request.html", {'mensaje2': "Usuario creado correctamente", 'form': form2 })
        else:
            form = UserRegisterForm()
            mensaje = "Los datos ingresados no son validos"
        
    else:
        form = UserRegisterForm()
        mensaje = "La contraseña debe incluir mayusculas y caracteres especiales"
        
    return render(request, 'register.html', {'form':form, 'mensaje':mensaje})




def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request,user)
                return redirect('home')
            
            else:
                form = AuthenticationForm()
                return render(request,"login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 1", 'form':form} )

        else:
            form = AuthenticationForm()
            return render(request,"login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 2", 'form': form} )

    else:

        form = AuthenticationForm()
        return render(request, 'login_request.html', {'form':form})
 
    
def profile_edit(request):
    
    usuario = request.user
    
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            
            # Datos a modificar:
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, 'profle_edit.html')
        
    else:
        form = UserEditForm(initial={'email':usuario.email})
        
    return render(request, 'profile_edit.html', {'form': form, 'usuario':usuario, 'email':usuario.email})


def profile(request):
    usuario = request.user
    avatar =  Avatar.objects.filter(user=usuario.id)
    context = {
        'username': usuario.username,
        'email': usuario.email,
        'avatar': avatar[0].image.url,
    }
    
    return render(request, 'profile.html', context)


