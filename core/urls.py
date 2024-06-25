from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),

    path('', views.home, name='home'), 
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'), 
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'), 
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),

    path('update-user/', views.update_user, name='update-user'), 

    path('topics/', views.topics_page, name='topics'),
    path('activities/', views.activities_page, name='activities'),
]