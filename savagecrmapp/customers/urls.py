from django.urls import path


from . import views


app_name = "customers"
urlpatterns = [
    #ex: /customers/
    path("", views.index, name="index"),
    #ex: /customers/5/detail/
    path("<int:customer_id>/detail/", views.detail, name="detail"),
    path("<int:service_id>/service/", views.services, name="service" ),
    path("<int:barber_id>/schedule/", views.schedule, name="schedule")
]