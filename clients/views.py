from django.shortcuts import render
from .models import Client, Monitoring
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import MonitoringForm


class ClientCreate(CreateView):
    model = Client
    template_name = 'client_create.html'
    success_url = reverse_lazy('client_create')
    fields = ['user', 'client_name', 'region', 'community', 'phone', 'email',
              'company', 'position', 'potential', 'passport_num', 'tax_code', 'comment']


@login_required
def clients(request):
    context = {'clients': Client.objects.filter(user_id=request.user.id)}
    return render(request, '../templates/clients.html', context)


@login_required
def client_details(request, pk):
    context = {'client': Client.objects.filter(id=pk)}
    return render(request, '../templates/client_details.html', context)


@login_required
def monitoring(request):
    form = MonitoringForm(request.POST)
    if request.method == "POST":
        form = MonitoringForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client']
            condition = form.cleaned_data['condition']
            details = form.cleaned_data['details']
            print(client_name)

            data_to_save = Monitoring(
                client_name=client_name, condition=condition, details=details)
            data_to_save.save()

            context = {'monitorings': Monitoring.objects.all(),

                       }

            return render(request, '../templates/monitoring_list.html', context)

    context = {'form': form}
    return render(request, '../templates/monitoring.html', context)


@login_required
def monitoring_list(request):
    context = {'monitorings': Monitoring.objects.all(),

               }

    return render(request, '../templates/monitoring_list.html', context)


@login_required
def monitoring_details(request, pk):
    context = {'monitoring': Monitoring.objects.filter(id=pk)}
    return render(request, '../templates/monitoring_details.html', context)
