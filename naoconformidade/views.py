from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core import mail
from datetime import datetime
import time
from .models import *
from .forms import NCForm
from .filters import NCFilter
from django.conf import settings
import folium
import geocoder
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd



def dashboard(request):
    item = NC.objects.all()
    total_TN = item.count()
    total_atendidas = item.filter(Situacao='A').count()
    total_nao_atendidas = item.filter(Situacao='P').count()
    myFilter = NCFilter(request.GET, queryset=item)
    item = myFilter.qs
    nc_list = NC.objects.values_list('latitude', 'longitude')

    map1 = folium.Map(location=[-27.13, -50.9219642], zoom_start=7)
    plugins.HeatMap(nc_list).add_to(map1)

    map1 = map1._repr_html_()

    context = {
        'item': item,
        'total_TN': total_TN,
        'total_atendidas': total_atendidas,
        'total_nao_atendidas': total_nao_atendidas,
        'myFilter': myFilter,
        'map1': map1,

    }

    return render(request, 'naoconformidade/dashboard.html', context)


def municipio(request):
    item = NC.objects.all()
    total_TN = item.count()
    total_atendidas = item.filter(Situacao='A').count()
    total_nao_atendidas = item.filter(Situacao='P').count()
    labels = total_atendidas
    data = total_nao_atendidas

    return render(request, 'naoconformidade/municipio.html', {
        'item': item,
        'total_TN': total_TN,
        'total_atendidas': total_atendidas,
        'total_nao_atendidas': total_nao_atendidas,
        'labels': labels,
        'data': data,

    })


def createNC(request):
    form = NCForm()
    if request.method == 'POST':
        form = NCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
            'form': form,
        }
    return render(request,'naoconformidade/NC_create.html', context)


ncs = NC.objects.all()
now = datetime.now().date()
for nc in ncs:
    if nc.Prazo >= now:
        send_mail('NC Vencida',
                  'Atenção!Verifique as suas NCs.',
                  'arisesch@gmail.com',
                  ['arisesch@gmail.com', 'francine@aris.sc.gov.br','marta@aris.sc.gov.br'], )
