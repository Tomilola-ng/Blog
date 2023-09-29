from django.contrib import admin
from api.models import  Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
