from django.contrib import admin
from home.models import FirstSlide


@admin.register(FirstSlide)
class FirstSlide(admin.ModelAdmin):
    list_display = ("slug",)
    search_fields = ("slug",)
    list_filter = ("slug",)
