from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.clients, name="clients"),
    path('monitoring/', views.monitoring, name="monitoring"),
    path('monitoring-list/', views.monitoring_list, name="monitoring-list"),
    path('monitoring_details/<int:pk>/',
         views.monitoring_details, name="monitoring_details"),
    path('client_details/<int:pk>/', views.client_details, name="client_details"),
    path('create/', login_required(views.ClientCreate.as_view()),
         name="client_create"),
]
