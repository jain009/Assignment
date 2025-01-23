from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User, ChatRoom, Message

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat.html', {'users': users})
