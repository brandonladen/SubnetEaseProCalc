from django.urls import path
from .views import login_user, logout_user, update_profile, signup_user

urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup_user, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('update_profile/', update_profile, name='update_profile'),
]
