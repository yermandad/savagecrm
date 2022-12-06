from django.urls import path


from . import views



urlpatterns = [
    #ex: /customers/
    path("", views.index, name="index"),
    #ex: /customers/5/detail/
    path("<int:customer_id>/detail/", views.detail, name="index"),
    path("<int:service_id>/service/", views.services, name="index" )
]   