from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name="calculate"),
    path('sale/', views.sale, name="sale_technology"),
    path('sale-fertilizer/', views.sale_fertilizer, name="sale_fertilizer"),

]
