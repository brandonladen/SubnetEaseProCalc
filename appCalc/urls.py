from django.urls import path
from .views import home,subnet, view_subnet_history, delete_subnet_history, landing_page

urlpatterns = [
    path('', landing_page, name="gettingstarted"),
    path('home/', home, name="home"),
    path('subnet/', subnet, name="subnet"),
    path('view_subnet_history/', view_subnet_history, name="view_subnet_history"),
    path('delete_subnet_history/<int:pk>/', delete_subnet_history, name="delete_subnet_history"),
]
