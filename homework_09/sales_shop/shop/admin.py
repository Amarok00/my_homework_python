from django.contrib import admin

from .models import Category
from .models import Product
from .models import Order
from .models import OrderPaymentDeteils


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "update_at"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description","archived"
    list_display_links = "id", "name"

class PaymentDetailsInlaine(admin.TabularInline):
    model = OrderPaymentDeteils

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        PaymentDetailsInlaine
    ]
    list_display = "id", "adress", "user", "promocode", "created_at"
    list_display_links = "id", "promocode"

    # fields = (
    #     "id",
    #     "adress",
    #     "user",
    #     "promocode",
    #     # "created_at",
    #     "payment_details",
    # )

@admin.register(OrderPaymentDeteils)
class OrderPaymentDeteilsAdmin(admin.ModelAdmin):
    list_display = "id", "payed_at", "card_ends_with", "status", "order"
    list_display_links = "id", "status"

