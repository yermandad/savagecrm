from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Customer
from django.views import generic
from django.utils import timezone

# Create your views here.


""" def index(request):
    latest_customer_list = Customer.objects.all()
    return  render(request, "customers/index.html", {
        "latest_customer_list": latest_customer_list
        })  #HttpResponse ("estas en la pagina principal de Savage App!")


def detail(request, customer_id):
    cliente= get_object_or_404(Customer, pk=customer_id)
    return  render(request, "customers/detail.html", {
            "customer": cliente 
        }) #HttpResponse(f"Estas viendo el historial del cliente no {customer_id}")


def services(request, service_id):
    return HttpResponse(f"Estas viendo el listado de clientes que han comprado el servicio no {service_id}")

def schedule(request, barber_id):
    return HttpResponse(f"Estas viendo el calendario del barbero no {barber_id}") """
    
class IndexView(generic.ListView):
    template_name= "customers/index.html"    
    context_object_name= "latest_customer_list"
    
    def get_queryset(self):
        return Customer.objects.order_by("-reg_date")[:5]

class DetailView(generic.DetailView):
    model= Customer
    template_name= "customers/detail.html"

class ServiceView(generic.DetailView):
    model= Customer
    template_name= "customers/service.html"
    
def schedule(request, barber_id):
    return HttpResponse(f"Estas viendo el calendario del barbero no {barber_id}")


def get_costumer(request):
    if request.method =='POST':
        search =request.POST.get('search')
        cliente=list(Customer.objects.values().filter(c_name__startswith=search))
        if(len(cliente)>0):
            data={'cliente':cliente}
        else:
            data={'message':'Not Found'}
        
        return JsonResponse(data)


def register_costumer(request):
    if request.method =='POST':
        c_name=request.POST.get('c_name')
        c_lastname=request.POST.get('c_lastname')
        c_phone=request.POST.get('c_phone')
        c_nickname= c_name+c_lastname[:2]
        c_password= c_nickname+'123'
        reg_date=timezone.now()
        cliente=Customer.objects.create(c_name=c_name, cl_lastname=c_lastname,c_phone=c_phone,c_nickname=c_nickname, c_password=c_password, reg_date=reg_date,)
        if(cliente):
            return HttpResponse(f'Cliente Registrado Satisfactoriamente')