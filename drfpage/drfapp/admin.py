from django.contrib import admin
from .models import Animal, Category
# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'time_create', 'time_update', 'is_published')
    list_display_links = ('title',)

admin.site.register(Category)