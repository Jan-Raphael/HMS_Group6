from django.contrib import admin
from .models import InventoryItem


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'reorder_level', 'price']


from django.contrib import admin

# Register your models here.
