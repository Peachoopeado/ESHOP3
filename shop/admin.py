from django.contrib import admin
from .models import Category, OilType, Viscosity, Compound, Fuel

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
