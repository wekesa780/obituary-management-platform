from django.contrib import admin
from .models import Obituary

@admin.register(Obituary)
class ObituaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death', 'author')
    search_fields = ('name', 'author')
    prepopulated_fields = {'slug': ('name',)}