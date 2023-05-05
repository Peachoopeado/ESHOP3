from django.contrib import admin
from .models import Favorite

# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    filter_horizontal = ['products']
admin.site.register(Favorite, FavoriteAdmin)

