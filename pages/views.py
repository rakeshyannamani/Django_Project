from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from . models import Page, Order


def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    #assert False
    return render(request, 'pages/page.html', context)


def getOrders(request):
    queryset_orders = Order.objects.all()[:20]
    queryset_cutomers = Order.objects.all()[:20]
    return JsonResponse({'orders': list(queryset_orders.values()), 'customers': list(queryset_cutomers.values())})
