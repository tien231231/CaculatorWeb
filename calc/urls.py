from django.urls import path
from .views import Cauculator

urlpatterns = [
    path('', Cauculator),
]