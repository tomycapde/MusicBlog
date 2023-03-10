from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
#from .models import Avatar


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            form.save()
            usuario = User.objects.get(username=name)
            profile = Profile.objects.create(user = usuario)
            profile.save()

            form2 = AuthenticationForm()
            return render(request,"users/login_request.html", {'mensaje2': "Usuario creado correctamente", 'form': form2 })
        else:
            form = UserRegisterForm()
            mensaje = "Los datos ingresados no son validos"
        
    else:
        form = UserRegisterForm()
        mensaje = "La contraseña debe incluir mayusculas y caracteres especiales"
        
    return render(request, 'users/register.html', {'form':form, 'mensaje':mensaje})


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
                return render(request,"users/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 1", 'form':form} )

        else:
            form = AuthenticationForm()
            return render(request,"users/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 2", 'form': form} )

    else:

        form = AuthenticationForm()
        return render(request, 'users/login_request.html', {'form':form})


@login_required
def user_edit(request):
    
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
            
            return render(request, 'users/profle_edit.html')
        
    else:
        form = UserEditForm(instance=usuario)
    
    return render(request, 'users/profile_edit.html', {'form': form, 'usuario':usuario, 'email':usuario.email})

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
        return render(request, 'users/profile_edit.html', {'form': form})







@login_required
def profile(request):
    usuario = request.user
    
    if usuario.profile.avatar:
        avatar = usuario.profile.avatar
    else:
        avatar = "avatars/user-logo.png"

    context = {
        'username': usuario.username,
        'email': usuario.email,
        'avatar': avatar,
        'bio': usuario.profile.bio,
        'website': usuario.profile.website,
    }
    
    return render(request, 'users/profile.html', context)


