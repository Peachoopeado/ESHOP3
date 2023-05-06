from django.contrib import admin
from .models import Category, Brand, OilType, Viscosity, Compound, Fuel, Product, CategoryImage, User_Request, Partner, \
    PartnerImage, Transmission
from import_export.admin import ImportExportMixin
from import_export import resources
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(Category)

admin.site.register(Brand)


class OilTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
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
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['category', 'oiltype', 'viscosity', 'compound', 'fuel']


admin.site.register(Transmission, TransmissionAdmin)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ['code']


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ['code', 'vendor_code', 'name_m', 'oiltype', 'compound', 'stock', 'price', 'available', 'img']
    list_editable = ['stock', 'price', 'available']
    list_filter = ['category', 'oiltype', 'viscosity', 'compound', 'available']
    filter_horizontal = ['category', 'viscosity', 'fuel', 'transmission']
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        from django.http import HttpResponse
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['code', 'vendor_code', 'name_m', 'name', 'oiltype', 'compound', 'price'])
        for obj in queryset:
            writer.writerow([obj.code, obj.name_m, obj.name, obj.oiltype, obj.compound, obj.price])
        return response
    export_as_csv.short_description = "Export Selected"


class PartnerAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryImage)
admin.site.register(User_Request)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerImage)
