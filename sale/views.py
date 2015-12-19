from django.shortcuts import render
import json
import utility

# Create your views here.
def sales_receipt_gen_engine(request):
    items, measuring_unit, price_chart = utility.get_todays_menu()
    offers = utility.get_todays_offers()
    orders = utility.get_latest_n_orders(5)

    return render(request, "sales_receipt_engine.html", {
        'items': json.dumps(items), 'orders': orders, 'offers': json.dumps(offers),
        'measuringUnit': json.dumps(measuring_unit), 'priceChart': json.dumps(price_chart)})