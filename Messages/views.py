from django.shortcuts import render, redirect
from .models import Message
from .forms import Message_Form, Respond_Form, RespondForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def all_messages(request):
    
    for_me = Message.objects.filter(receiver=request.user)
    from_me = Message.objects.filter(sender=request.user)
    
    context = {
        'for_me': for_me,
        'from_me':from_me,
    }
    
    return render(request, 'messages/bandeja.html', context)

@login_required
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
                message.subject = form.cleaned_data['subject']
                message.content = str(form.cleaned_data['content'])
                message.seen = False 

                message.save()

                print('EXISTE')
                
                return redirect('all_messages')
                    
            except User.DoesNotExist:
                
                print('NO EXISTE')
                
                error_message = f"El usuario {receiver} no existe"
                form = Message_Form()
            
                return render(request, 'messages/nuevo_mensaje.html',{'form':form, 'error_message':error_message})
        else:
            form = Message_Form()    
    else:
        form = Message_Form()
    
    return render(request, 'messages/nuevo_mensaje.html',{'form':form})

@login_required
def chat(request, id):
    message = Message.objects.get(id=id)

    message.seen = True
    message.save()


    return render(request, 'messages/chat.html', {'message': message}) 

'''
@login_required
def respond_message(request, receiver):
    if request.method == 'POST':
        
        form = Respond_Form(request.POST)
        
        if form.is_valid():
            
            receiver = form.cleaned_data['receiver']
            
            try:
                user = User.objects.get(username=receiver)
                
                message = Message.objects.create()
                message.sender = str(request.user)
                message.receiver = receiver
                message.content = str(form.cleaned_data['content'])
                message.seen = False 

                message.save()

                print('EXISTE')
                
                return redirect('all_messages')
                    
            except User.DoesNotExist:
                
                print('NO EXISTE')
                
                error_message = f"El usuario {receiver} no existe"
                form = Respond_Form()
                return render(request, 'messages/responder_mensaje.html',{'form':form, 'error_message':error_message, 'receiver':receiver, 'subject': subject})
        else:
            form = Respond_Form()    
    else:
        form = Respond_Form()
    return render(request, 'messages/responder_mensaje.html',{'form':form, 'receiver':receiver, 'subject': subject})
'''


def respond_message(request, receiver):
    #sender = request.user.username
    mensaje = Message.objects.create(sender = request.user.username, receiver = receiver)
    
    if request.method == 'POST':
        form = RespondForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect('all_messages')
    else:
        form = RespondForm(instance=mensaje)
        return render(request, 'messages/responder_mensaje.html', {'form': form, 'receiver': receiver})




