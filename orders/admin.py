from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_code_fields = ['products']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'full_name', 'email',
                    'address', 'postal_code', 'way_to_get', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
