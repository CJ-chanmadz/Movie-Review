from django.urls import path
from . import views
from .views import Request

urlpatterns = [
   path('', views.request, name='request')
]