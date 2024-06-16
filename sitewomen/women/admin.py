from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','is_published','cat')
    # Кликабельность поля
    # list_display_links = ('id','title')
    list_display_links = ('id',)
    ordering = ['-time_create','title']
    list_editable = ('is_published', 'title','cat')
    list_per_page = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    # Кликабельность поля
    list_display_links = ('id','name')



# admin.site.register(Women, WomenAdmin)