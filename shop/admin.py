from django.contrib import admin
from .models import Category, Brand, OilType, Viscosity, Compound, Fuel, Product, CategoryImage, ProductImage, User_Request, Partner, PartnerImage, Transmission
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)

admin.site.register(Brand)

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

class TransmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}
    filter_horizontal = ['category', 'oiltype', 'viscosity', 'compound', 'fuel']

admin.site.register(Transmission, TransmissionAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','vendor_code','name_m','oiltype', 'compound', 'stock', 'price', 'available']
    list_editable = ['stock', 'price', 'available']
    list_filter = ['category','oiltype', 'viscosity', 'compound',  'available']
    filter_horizontal = ['category', 'viscosity', 'fuel', 'transmission']

class PartnerAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryImage)
admin.site.register(ProductImage)
admin.site.register(User_Request)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerImage)