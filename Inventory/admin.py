from django.contrib import admin
from .models import *


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_code', 'price', 'brand_id', 'status', 'datetime')
    search_fields = ('item_name', 'item_code', 'brand_id')
    list_filter = ('brand_id', 'status')
    ordering = ('-datetime',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'mobile_no', 'address', 'status')
    search_fields = ('supplier_name', 'mobile_no')
    list_filter = ('status',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'invoice_date', 'supplier', 'total_amount', 'status', 'datetime')
    search_fields = ('invoice_no', 'supplier__supplier_name')
    list_filter = ('status', 'datetime')
    date_hierarchy = 'datetime'

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'invoice_date', 'customer_name', 'number', 'totalamount', 'status', 'datetime')
    search_fields = ('invoice_no', 'customer_name', 'number')
    list_filter = ('status', 'datetime')
    date_hierarchy = 'datetime'



@admin.register(PurchaseDetail)
class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ('purchase_master', 'item', 'quantity', 'price', 'amount', 'status', 'datetime')
    search_fields = ('purchase_master__invoice_no', 'item__item_name')
    list_filter = ('status', 'datetime')
    date_hierarchy = 'datetime'
