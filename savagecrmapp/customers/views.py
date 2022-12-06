from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse ("estas en la pagina principal de Savage App!")


def detail(request, customer_id):
    return HttpResponse("Estas viendo el historial del cliente no {customer_id}")


def services(request, service_id):
    return HttpResponse("Estas viendo el listado de clientes que han comprado el servicio no {service_id}")