from django.urls import path
from .views import ListUsers,Register,Logout

urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',ListUsers.as_view()),
    path('logout/',Logout.as_view()),
]
