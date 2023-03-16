from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    #ex: /customers/
    path("", views.IndexView.as_view(), name="index"),
    #ex: /customers/5/detail/
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/service/", views.ServiceView.as_view(), name="service" ),
    path("<int:barber_id>/schedule/", views.schedule, name="schedule"),
    
    #link de consulta ajax
    path("consulta/",views.get_costumer, name="consulta")
]