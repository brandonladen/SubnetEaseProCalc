from django.urls import path
from .views import login_user, logout_user, update_profile

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update_profile/', update_profile, name='update_profile'),
]
