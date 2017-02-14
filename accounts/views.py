from django.conf import settings
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import UserLoginForm,UserRegisterForm
from accounts.models import Game
from accounts.chess import Chess

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
        g = Game ( user = user )
        g.save ()
        return redirect("/game")
    context={
        "form":form,
        "title":title
    }

    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return render(request, "form.html",{})



def game_view(request):
    user=request.user
    content={}
    game = Game.objects.get(user=user)
    state_list = request.user.game.state.split('/')

    if ( request.method == "POST" ):

        user_move = request.POST.get ( 'move' )
        test=Chess(game.state)

        user_movel = list(map(int, user_move.split()))
        origin = user_movel[:2]
        dist = user_movel[2:]

        state_list=test.state_list

        if test.is_valid(origin,state_list,dist)==False:

            content['error']="Your move isn't valid"
        else:
            user_movel  = list(map ( int, user_move.split ()))
            origin= user_movel[:2]
            dist=user_movel[2:]

            state_list=test.update_state_with_move(origin,state_list,dist)
            print(state_list)
            AI_move=test.minimax(state_list,3,"AI")[1]
            print("AI",AI_move)
            game.state = AI_move
            game.save()
    #state_list = request.user.game.state.split('/')

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
    list2=[]

    for i in range (0,len(state_list)):
        for j in range(0,len(state_list[i])):
            if "A"<state_list[i][j]<"Z" or "a"<state_list[i][j]<"z":
                list2.append(state_list[i][j])


    for i in list2:
        list1.append([])
        for j in i:
            list1[-1].append(chess_pieces_dict[j])

    final_state_list=[]

    final_state_list.append(list1[:8])
    final_state_list.append(list1[8:16])
    final_state_list.append(list1[16:24])
    final_state_list.append(list1[24:32])
    final_state_list.append(list1[32:40])
    final_state_list.append(list1[40:48])
    final_state_list.append(list1[48:56])
    final_state_list.append(list1[56:])


    content["final_state_list"]=final_state_list


    return render(request, "personal/game.html",content)
