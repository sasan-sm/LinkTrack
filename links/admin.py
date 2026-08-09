from django.contrib import admin
from .models import ShortLink, Click


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('owner', 'slug', 'created_at')

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('link', 'clicked_at')