from django.shortcuts import render
from django.http import JsonResponse


def calculate_price_incl_tax(request):
    price_excl_tax = float(request.GET.get("price_excl_tax", 0))
    tax_rate = float(request.GET.get("tax_rate", 0))
    price_incl_tax = price_excl_tax * (1 + tax_rate / 100)
    return JsonResponse({"price_incl_tax": price_incl_tax})


def calculator_view(request):
    return render(request, "calculator.html")
