from django.contrib import admin

# Register your models here.
from .models import *


class GuardianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'age', 'sex', 'city', 'volume', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone_number', 'address')
    """list_editable = ('status',)"""
    list_filter = ('age', 'time_create', 'city')


class GuardianCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_type', 'name', 'phone_number', 'inn', 'kpp', 'ogrn', 'volume', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone_number', 'address_ur', 'address_real')
    """list_editable = ('status',)"""
    list_filter = ('company_type', 'time_create', 'city')


class SlaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'age', 'sex', 'city', 'volume_need', 'volume_get', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone_number', 'address')
    """list_editable = ('status',)"""
    list_filter = ('age', 'time_create', 'city')


admin.site.register(Guardian, GuardianAdmin)
admin.site.register(GuardianCompany, GuardianCompanyAdmin)
admin.site.register(Slave, SlaveAdmin)
