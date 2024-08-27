from django.shortcuts import render
from django.template.response import TemplateResponse


def format_parameters(params):
    for q in ["price_excl_tax", "price_incl_tax", "tax_rate"]:
        params[q] = float(params[q])
    return params


def calculator_view(request):
    if request.method == "POST":
        params = format_parameters(request.POST)
        updated_input = params["updated_input"]
        if updated_input == "price_excl_tax" or updated_input == "tax_rate":
            params["price_incl_tax"] = params["price_excl_tax"] * (
                1 + params["tax_rate"] / 100
            )
        elif updated_input == "price_incl_tax":
            params["price_excl_tax"] = params["price_incl_tax"] / (
                1 + params["tax_rate"] / 100
            )

    return TemplateResponse(request, "calculator.html", params)
