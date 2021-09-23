from django.contrib import admin

from .models import Player

class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    class Meta:
        model = Player

admin.site.register(Player,PlayerModelAdmin)
