from django.urls import path,include
from . import views
urlpatterns = [
    path('idu',views.index,name='index'),
    path('navbar',views.navbar,name='navbar'),
    path('booking',views.booking,name='booking'),
    path('k',views.booku,name='booku'),
    path('enter-info/', views.enter_info, name='enter_info'),
    path('enter-marks/', views.enter_marks, name='enter_marks'),
    path('/', views.get_marks, name='get_marks'),
]


