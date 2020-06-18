from django.shortcuts import render
from .models import Fertilizer
from clients.models import Client
from sales.models import Sale
from .forms import CalculationForm, SaleFretilizerForm
from django.contrib.auth.decorators import login_required


calc_data = {}


@login_required
def calculate(request):
    form = CalculationForm(request.POST)
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client']
            area = form.cleaned_data['area']
            group_type = form.cleaned_data['group_type']

            if group_type == 'grape_main':
                ferts = Fertilizer.objects.all().exclude(fertilizer_name='Carbon plus')

                prices = []

                for fert in ferts:
                    prices.append(
                        int(fert.price*fert.expense_norm*area))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(prices),
                           'area': area
                           }
                calc_data = context
                calc_data['group_type'] = group_type

                return render(request, '../templates/calculation.html', context)

            elif group_type == 'grape_simple':
                ferts = Fertilizer.objects.all().filter(fertilizer_name__in=[
                    'Carbon plus', 'Rampart', 'Fostrak', 'Active Flower(PolinAid)'])

                prices = []

                for fert in ferts:
                    prices.append(
                        int(fert.price*fert.expense_norm*area))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(prices),
                           'area': area
                           }

                calc_data = context
                calc_data['group_type'] = group_type

                return render(request, '../templates/calculation.html', context)

            elif group_type == 'potato':
                ferts = Fertilizer.objects.all().filter(fertilizer_name__in=[
                    'Carbon plus', 'Rampart', 'Fostrak'])

                prices = []

                for fert in ferts:
                    prices.append(
                        int(fert.price*fert.expense_norm*area))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(prices),
                           'area': area
                           }

                return render(request, '../templates/calculation.html', context)

    context = {'fertilizers': Fertilizer.objects.all(),
               'form': form
               }
    return render(request, '../templates/calculate.html', context)


@login_required
def sale(request):
    form = CalculationForm(request.POST)
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client']
            area = form.cleaned_data['area']
            group_type = form.cleaned_data['group_type']

            if group_type == 'grape_main':
                ferts = Fertilizer.objects.all().exclude(fertilizer_name='Carbon plus')

                total_sum = []

                for fert in ferts:

                    data_to_save = Sale(client=client_name, client_name=client_name, fertilizer=fert.fertilizer_name, area=area, sale_qty=float(area*fert.expense_norm), total_sum=int(
                        fert.price*area*fert.expense_norm), group_type=group_type)
                    data_to_save.save()

                    total_sum.append(int(
                        fert.price*area*fert.expense_norm))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(total_sum),
                           'area': area
                           }

                return render(request, '../templates/saled_fertilizers.html', context)

            elif group_type == 'grape_simple':
                ferts = Fertilizer.objects.all().filter(fertilizer_name__in=[
                    'Carbon plus', 'Rampart', 'Fostrak', 'Active Flower(PolinAid)'])

                total_sum = []

                for fert in ferts:

                    data_to_save = Sale(client=client_name, client_name=client_name, fertilizer=fert.fertilizer_name, area=area, sale_qty=float(area*fert.expense_norm), total_sum=int(
                        fert.price*area*fert.expense_norm), group_type=group_type)
                    data_to_save.save()

                    total_sum.append(int(
                        fert.price*area*fert.expense_norm))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(total_sum),
                           'area': area
                           }

                return render(request, '../templates/saled_fertilizers.html', context)

            elif group_type == 'potato':
                ferts = Fertilizer.objects.all().filter(fertilizer_name__in=[
                    'Carbon plus', 'Rampart', 'Fostrak'])

                total_sum = []

                for fert in ferts:

                    data_to_save = Sale(client=client_name, client_name=client_name, fertilizer=fert.fertilizer_name, area=area, sale_qty=float(area*fert.expense_norm), total_sum=int(
                        fert.price*area*fert.expense_norm), group_type=group_type)
                    data_to_save.save()

                    total_sum.append(int(
                        fert.price*area*fert.expense_norm))

                context = {'client_name': client_name,
                           'ferts': ferts,
                           'total': sum(total_sum),
                           'area': area
                           }

                return render(request, '../templates/saled_fertilizers.html', context)

    context = {'form': form}
    return render(request, '../templates/sale_technology.html', context)


@login_required
def sale_fertilizer(request):
    form = SaleFretilizerForm(request.POST)
    if request.method == 'POST':
        form = SaleFretilizerForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client']
            fertilizer = form.cleaned_data['fertilizer']
            sale_qty = form.cleaned_data['sale_qty']

            fert = Fertilizer.objects.get(fertilizer_name=fertilizer)

            data_to_save = Sale(client=client_name, client_name=client_name,
                                fertilizer=fert.fertilizer_name, sale_qty=sale_qty, total_sum=fert.price*sale_qty)
            data_to_save.save()

            context = {'client_name': client_name,
                       'fert': fert,
                       'total': fert.price*sale_qty,
                       'qty': sale_qty
                       }

            return render(request, '../templates/single_saled_fertilizers.html', context)

    context = {'form': form
               }
    return render(request, '../templates/sale_technology.html', context)
