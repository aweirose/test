from django.urls import path
from wechat import views

urlpatterns = [
    path('link/', views.link),
    path('rose/', views.WeixinView),
]
