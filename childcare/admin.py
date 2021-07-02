from django.contrib import admin

from core.utils import get_all_fields

from .models import Childcare


class ChildcareAdmin(admin.ModelAdmin):
    list_display = get_all_fields(Childcare)
    # fields=['name']
    list_display_links = ["approval_number", "name"]
    # filter_horizontal = [""]


admin.site.register(Childcare, ChildcareAdmin)
