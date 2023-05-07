from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
# Register your models here.

def order_payment(obj):
    url = obj.get_string_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_payment.short_description = "Stripe payment"

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "address", "postal_code", "city", "paid", "created", "updated"]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInLine]

