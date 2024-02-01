from django.contrib import admin
from sel_pre_related import models as sel_pre_related_models


# Register your models here.
@admin.register(sel_pre_related_models.Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price"]


@admin.register(sel_pre_related_models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]


@admin.register(sel_pre_related_models.Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]
