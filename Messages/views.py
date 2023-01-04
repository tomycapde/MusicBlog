from django.shortcuts import render, redirect
from .models import Message
from .forms import Message_Form

# Create your views here.
def all_messages(request):
    pass



def new_message(request):
    if request.method == 'POST':
        
        form = Message_Form(request.POST)
        
        if form.is_valid():
            message = Message.objects.create()
            message.sender = str(request.user)
            message.receiver = form.cleaned_data['receiver']
            message.content = form.cleaned_data['content']
            message.seen = False 

            message.save()
    
            return redirect('home')
        
        else:
            form = Message_Form()    
    else:
        form = Message_Form()
    return render(request, 'prueba_mensaje.html',{'form':form})


def chat(request, id):
    pass