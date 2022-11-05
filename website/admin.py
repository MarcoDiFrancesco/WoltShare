from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "seller",
        "quantity",
        "price_per_quant",
        "description",
        "type",
        "packaging",
    )
