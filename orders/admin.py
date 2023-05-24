from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_code_fields = ['products']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['manager_status', 'id', 'type', 'full_name', 'email',
                    'address', 'way_to_get', 'get_total_cost', 'paid',
                    'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated']
    
    def get_total_cost(self, obj):
        return obj.get_total_cost()
    get_total_cost.short_description = 'Total Cost'

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
