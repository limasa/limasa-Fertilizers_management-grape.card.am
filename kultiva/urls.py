from django.contrib import admin
from django.urls import path, include
from fertilizers.views import LoginView, LogoutView, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='main'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('clients/', include('clients.urls')),
    path('calculate/', include('sales.urls')),
    path('fertilizers/', include('fertilizers.urls')),
]
