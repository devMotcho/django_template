from django.urls import path
from .views import (
    homeView,
)
from .authentication import (
    loginPage,
    logoutUser,
)
app_name = 'app'

urlpatterns = [
    path('', homeView, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]