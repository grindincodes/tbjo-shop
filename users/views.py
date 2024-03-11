from logging import raiseExceptions
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import *
from .forms import UserSignupForm, EmailAuthenticationForm
# for kakao login
from django.conf import settings
import random
from django.utils import timezone
from datetime import datetime
# Create your views here.

# 이메일 회원가입
def signup_email(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 생성, 저장 완료 # 이메일이 중복되었는지는 폼에서 따로 체크하도록 구현(현재 유저네임필드는 닉네임이라 인증을 따로 만들었음.)
            login(request, user, backend='users.mybackend.MyBackend') # https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'signup_email.html', {'form':form})

# 이메일로 로그인
def email_login(request):
    if request.method=="POST":
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            # form 에서 인증 한번, 오류input 잡아주기 위해서!
            if form.authenticate_login():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                # 실제 로그인 전 인증
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user, backend='users.mybackend.MyBackend') # https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in
                    request.user.last_login= timezone.now()
                    return redirect('home')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'email_login.html', {'form':form})



def logout_view(request):
    # logout: Remove the authenticated user's ID from the request and flush their session data.
    logout(request)
    # 이전 state를 그대로 get에 담아 전달해줄 수 있기 때문에, 여기서 state정보를 확인하고
    # redirect를 어디로 할지 정할 수 있음
    # 구현 예시: if request.GET.get("state") is not None: return redirect('detail', state에 담긴 pk값)
    return redirect('home')