from django.urls import path
from .views import *


urlpatterns= [
    # 주문 페이지 및 주문 내역 페이지
    path('product/<int:product_pk>/order', order, name="order"), # view에서 .create_user(...) 사용해야 함.
    path('<int:order_pk>/complete', complete, name="complete"),
    path('all', all, name="all"),
]