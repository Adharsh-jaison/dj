from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('register',views.register,name="register"),
    path('login/',views.login,name='login'),
    path("user_register",views.user_register,name='user_register'),
    path("user_login",views.user_login,name='user_login'),
]