from django.urls import path

from . import views
from .views import RegisterUser, LoginUser, Getusers, DeleteUser

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login/', LoginUser.as_view(), name='login'),
    path('getusers/', Getusers.as_view(), name="users"),
    path('deleteuser/', DeleteUser.as_view(), name="deleteuser")
]
