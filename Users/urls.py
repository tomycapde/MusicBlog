from django.urls import path

from .views import register, login_request, profile_edit, profile, user_edit

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request, name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('user_edit/', user_edit, name='user_edit'),
]
