from django.contrib import admin

from .models import Moeda


@admin.register(Moeda)
class MoedaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "initials",
        "name_coin",
        "data",
        "value",
    ]
