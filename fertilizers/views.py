from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Fertilizer
from django.contrib.auth.decorators import login_required


class LandingPageView(TemplateView):
    template_name = 'main.html'


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = 'fertilizers.html'


class LogoutView(LogoutView):
    success_url = 'main.html'


@login_required
def fertilizers(request):

    context = {'fertilizers': Fertilizer.objects.all()}

    return render(request, '../templates/fertilizers.html', context)
