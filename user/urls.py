from django.urls import path
from user.views import user_login, user_logout


app_name = "user"

urlpatterns = [
    path("",user_login,name="user_login"), 
    path("user_logout",user_logout,name="user_logout") 
]