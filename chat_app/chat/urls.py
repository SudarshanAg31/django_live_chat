from django.urls import path
from . import views;

urlpatterns = [
    path("",views.index,name='index'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getmessages/<str:pk>/',views.getmessages,name='getmessages'),
    path('<str:pk>/',views.room,name='room')
]
