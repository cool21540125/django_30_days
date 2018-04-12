from django.contrib import admin

# Register your models here.
from .models import Store, MenuItem

# admin.site.register(Store)

# https://github.com/uranusjr/django-tutorial-for-programmers/blob/1.8/08-django-admin.md
# 把兩個 Model做 inline的關係(用來做內嵌頁面)
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes',)
    inlines = (MenuItemInline,)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)






