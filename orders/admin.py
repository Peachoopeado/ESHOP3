from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_code_fields = ['products']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['manager_status', 'id', 'type', 'full_name', 'email',
                    'address', 'way_to_get', 'paid',
                    'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
