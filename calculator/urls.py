from django.urls import path
from .views import calculator_view, calculate_price_incl_tax

urlpatterns = [
    path("", calculator_view, name="calculator_view"),
    path("calculate/", calculate_price_incl_tax, name="calculate_price_incl_tax"),
]
