from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('musician_list/', views.musician_list, name='musician_list'),
    path('musician/<int:id>/', views.musician_detail, name='musician_detail'),
    path('album/<int:id>/', views.album_detail, name='album_detail'),
    path('song/<int:id>/', views.song_detail, name='song_detail'),
]
