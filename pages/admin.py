from django.contrib import admin
from .models import Page, Customer, Product, Order


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
