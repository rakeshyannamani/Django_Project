from django.contrib import admin
from .models import Page, Company, Programmers, Language


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)

admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Programmers)
