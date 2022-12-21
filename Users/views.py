from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            form2 = AuthenticationForm()
            return render(request,"login_request.html", {'mensaje2': "Usuario creado correctamente", 'form': form2 })
        else:
            form = UserRegisterForm()
        
    else:
        form = UserRegisterForm()
        
    return render(request, 'register.html', {'form':form})




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


