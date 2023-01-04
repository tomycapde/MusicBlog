from django.shortcuts import render, redirect
from .models import Message
from .forms import Message_Form
from django.contrib.auth.models import User

# Create your views here.
def all_messages(request):
    
    #mensajes = Message.objects.filter(receiver=request.user)
    for_me = Message.objects.filter(receiver=request.user)
    from_me = Message.objects.filter(sender=request.user)
    
    context = {
        'for_me': for_me,
        'from_me':from_me,
        #'mensajes':mensajes
    }
    
    return render(request, 'prueba_bandeja.html', context)



def new_message(request):
    if request.method == 'POST':
        
        form = Message_Form(request.POST)
        
        if form.is_valid():
            
            receiver = form.cleaned_data['receiver']
            
            try:
                user = User.objects.get(username=receiver)
                
                message = Message.objects.create()
                message.sender = str(request.user)
                message.receiver = form.cleaned_data['receiver']
                #message.content = form.cleaned_data['content']
                message.content = str(form.cleaned_data['content'])
                message.seen = False 

                message.save()

                print('EXISTE')
                
                return redirect('home')
                    
            except User.DoesNotExist:
                
                print('NO EXISTE')
                
                error_message = f"El usuario {receiver} no existe"
                form = Message_Form()
                return render(request, 'prueba_mensaje.html',{'form':form, 'error_message':error_message})
        else:
            form = Message_Form()    
    else:
        form = Message_Form()
    return render(request, 'prueba_mensaje.html',{'form':form})






def chat(request, id):
    
    message = Message.objects.get(id=id)

    message.seen = True
    message.save()

    return render(request, 'prueba_chat.html', {'message':message})