from django.urls import path
from .views import (
    homeView,
)
app_name = 'app'

urlpatterns = [
    path('', homeView, name='home'),
]