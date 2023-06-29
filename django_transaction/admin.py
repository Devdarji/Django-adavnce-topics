from django.contrib import admin

from django_transaction import models as django_transaction_models


# Register your models here.


@admin.register(django_transaction_models.UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    list_display = ["user", "balance", "created_at", "updated_at"]


@admin.register(django_transaction_models.Transfer)
class TransferAdmin(admin.ModelAdmin):
    search_fields = ["initiated_by", "transfer_to"]
    list_display = ["initiated_by", "transfer_to", "amount", "created_at", "updated_at"]


@admin.register(django_transaction_models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ["course_name"]
    list_display = ["course_name"]
