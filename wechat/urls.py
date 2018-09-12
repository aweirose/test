from django.conf.urls import url
from wechat import views

urlpatterns = [
    url('link/', views.link),
    url('rose/', views.WeixinView.as_view()),
]
