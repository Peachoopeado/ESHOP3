from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(models.MainPartner)
admin.site.register(models.MainPartnerImg)


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text')


admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsImage)
