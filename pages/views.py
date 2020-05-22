from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import JsonResponse
import random
from django.views.generic import View
from . models import Page, Order

User = get_user_model()


def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)


def getOrders(request):
    queryset_orders = Order.objects.all()[:20]
    queryset_cutomers = Order.objects.all()[:20]
    return JsonResponse({'orders': list(queryset_orders.values()), 'customers': list(queryset_cutomers.values())})


def chartData(request):
    qs_count = User.objects.all().count()
    labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = [qs_count, 10, 20, 30, 40]
    data = {
        "labels": labels,
        "default": default_items,
    }
    return JsonResponse(data)

# def chartRand(request):
#     rand_num = random.randint(10, 90)
#     return JsonResponse({'rand_num': rand_num})
