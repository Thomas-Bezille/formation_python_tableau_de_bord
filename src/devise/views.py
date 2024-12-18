from django.shortcuts import render

import api


# Create your views here.
def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days_range=days_range)

    return render(request, "devise/index.html", context={
        "data": rates,
        "days_labels": days
    })