from django.contrib import admin
from .models import Share


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = (
        "form_name",
        "created",
    )
