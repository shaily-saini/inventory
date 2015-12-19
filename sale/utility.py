__author__ = 'shaily.saini'
import datetime
from models import Custorder, Item, Itemmeasuringunit, Itempricechart, Offer, Offeritem, custOrderItems

def get_todays_menu():
    items = Item.objects.filter(isvalid=True)
    item_ids = items.values_list('itemid', flat=True)
    measuring_units = Itemmeasuringunit.objects.filter(isvalid=True, itemid__in=list(item_ids))
    measuring_units_ids = measuring_units.values_list('itemmeasuringunitid')
    measuring_units_list = measuring_units.values_list('itemid', 'measuringunitid__measuringunitname', 'itemmeasuringunitid', 'measuringunitid__measuringunitid')
    item_list = items.values_list('itemid', 'itemuniquekey', 'itemname', 'isavailable')
    price_chart_list = Itempricechart.objects.filter(itemmeasuringunitid__in=list(measuring_units_ids)).values_list('itemmeasuringunitid__itemid__itemid', 'itemmeasuringunitid__measuringunitid__measuringunitid', 'qty', 'price')
    item_map = {}
    for item in item_list:
        item_map[item[0]] = {}
        item_map[item[0]]['key'] = item[1]
        item_map[item[0]]['name'] = item[2]
        item_map[item[0]]['isAvailable'] = item[3]
    measuring_unit_map = {}
    for unit in measuring_units_list:
        if unit[0] not in measuring_unit_map.keys():
            measuring_unit_map[unit[0]] = {}
            measuring_unit_map[unit[0]]['units'] = []
        measuring_unit_map[unit[0]]['units'].append({'name': unit[1], 'measurementId': unit[3], 'maptoprice': unit[2]})
    price_chart_map = {}
    for price in price_chart_list:
        if price[0] not in price_chart_map.keys():
            price_chart_map[price[0]] = {}
        price_chart_map[price[0]][price[1]] = price[3]
    return item_map, measuring_unit_map, price_chart_map

def get_todays_offers():
    offer_items = Offeritem.objects.filter(offerid__validfrom__gte=datetime.date.today(), offerid__validtill__gte=datetime.date.today())
    offer_items_list = offer_items.values_list('offerid', 'itemid', 'offerid__offername', 'offerid__discountrate')
    item_offer_map = {}
    for offer in offer_items_list:
        if offer[1] not in item_offer_map.keys():
            item_offer_map[offer[1]] = {}
            item_offer_map[offer[1]]['offer_name'] = offer[2]
            item_offer_map[offer[1]]['discount'] = offer[3]
        else:
            if offer[3] > item_offer_map[offer[1]]['discount']:
                item_offer_map[offer[1]]['offer_name'] = offer[2]
                item_offer_map[offer[1]]['discount'] = offer[3]
    return item_offer_map

def get_order_items(order_id):
    order_items = custOrderItems.objects.filter(custorderid=order_id)
    items_map = {}
    for order_item in order_items:
        items_map[order_item.itemid] = {}
        items_map[order_item.itemid]['itemName'] = order_item.itemid.itemname
        items_map[order_item.itemid]['qty'] = order_item.qty
        items_map[order_item.itemid]['unit'] = order_item.measuringunitid
        items_map[order_item.itemid]['priceperunit'] = order_item.priceperunit
        if order_item.offeridavailed is not None:
            items_map[order_item.itemid]['offerAvailed'] = {}
            items_map[order_item.itemid]['offerAvailed']['offerName'] = order_item.offeridavailed.offername
            items_map[order_item.itemid]['offerAvailed']['discountRate'] = order_item.offeridavailed.discountrate
        else:
            items_map[order_item.itemid]['offerAvailed'] = None
        items_map[order_item.itemid]['offerpriceperunit'] = order_item.offerpriceperunit
        items_map[order_item.itemid]['totalPrice'] = order_item.price
    return items_map

def get_latest_n_orders(num_of_orders):
    orders = Custorder.objects.all().order_by('-custorderid')[0:num_of_orders]
    orders = orders.values_list('custorderid', 'custordernum', 'custorderdate', 'discount', 'originalamount', 'totalamount')
    order_list = []
    for order in orders:
        order_map = {}
        order_map['items'] = get_order_items(order[0])
        order_map['orderNum'] = order[1]
        order_map['date'] = order[2]
        order_map['discount'] = order[3]
        order_map['originalAmount'] = order[4]
        order_map['totalAmount'] = order[5]
        order_list.append(order_map)
    return order_list