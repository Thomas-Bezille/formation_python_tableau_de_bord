from django.shortcuts import render, redirect

import api


# Create your views here.
def redirect_index(request):
    return redirect("home", currencies="EUR", days_range=30)

def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days_range=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "devise/index.html", context={
        "data": rates,
        "days_labels": days,
        "currencies": currencies,
        "page_label": page_label
    })