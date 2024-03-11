from django.urls import path
from .views import *


urlpatterns= [
    # 로그인 홈 화면, 이메일 가입, 로그인
    path('signup/email', signup_email, name="signup_email"), # view에서 .create_user(...) 사용해야 함.
    path('login/email', email_login, name="email_login"), # 이메일로 authenticate()
    path('logout', logout_view, name="logout"), # user logout 시키기
]