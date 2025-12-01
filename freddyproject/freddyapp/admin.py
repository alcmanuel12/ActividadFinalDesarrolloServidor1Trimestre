from django.contrib import admin
from .models import Animatronic, Party

admin.site.register(Party)

@admin.register(Animatronic)
class AnimatronicAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal', 'build_date', 'decommissioned')
    list_filter = ('animal', 'decommissioned')
    search_fields = ('name',)