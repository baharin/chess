from django.conf import settings
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import UserLoginForm,UserRegisterForm


def login_view(request):
    title= "Login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username, password=password)
        login(request,user)
        return redirect("/game")
    return render(request, "form.html", {"form":form, "title":title})


def register_view(request):
    title="Register"
    form= UserRegisterForm(request.POST or None)
    if form.is_valid():
        user= form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        subject= 'Confirmation Email'
        message= 'Thanks for registering in my site. Hope you enjoy playing chess!'
        from_email=settings.EMAIL_HOST_USER
        to_list=[user.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        login(request, user)
        return redirect("/game")
    context={
        "form":form,
        "title":title
    }

    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return render(request, "form.html", {})


def game_view(request):
    default_state = "RNBQKBNRPPPPPPPPeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeepppppppprnbqkbnr"
    state_list = []
    for i in range(0, 8):
        state_list.append(default_state[8 * i:8 * i + 9])
    chess_pieces_dict={
        "b":"b0.png",
        "k":"k0.png",
        "n":"n0.png",
        "p":"p0.png",
        "q":"q0.png",
        "r":"r0.png",
        "B": "b1.png",
        "K": "k1.png",
        "N": "n1.png",
        "P": "p1.png",
        "Q": "q1.png",
        "R": "r1.png",
        "e":"e.png",
    }
    list1=[]
    for i in state_list:
        list1.append([])
        for j in i:
            list1[-1].append(chess_pieces_dict[j])




    return render(request, "personal/game.html",{'list1':list1})