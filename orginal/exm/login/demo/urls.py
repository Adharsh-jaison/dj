from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('index',views.index,name='index'),
    path('login/',views.login,name='login'),
    path("user_register",views.user_register,name='user_register'),
    path("user_login",views.user_login,name='user_login'),
]