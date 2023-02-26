from django.contrib import admin
from .models import Category, OilType, Viscosity, Compound, Fuel, Product

# Register your models here.
admin.site.register(Category)

class OilTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ['category']

admin.site.register(OilType, OilTypeAdmin)

class ViscosityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['category', 'oiltype']

admin.site.register(Viscosity, ViscosityAdmin)

class CompoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['category', 'oiltype', 'viscosity']

admin.site.register(Compound, CompoundAdmin)


class FuelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['category', 'oiltype', 'viscosity', 'compound']

admin.site.register(Fuel, FuelAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','vendor_code','name_m','oiltype', 'viscosity', 'compound', 'fuel', 'stock', 'price', 'available']
    list_editable = ['stock', 'price', 'available']
    list_filter = ['category','oiltype', 'viscosity', 'compound', 'available']
    filter_horizontal = ['category']


admin.site.register(Product, ProductAdmin)