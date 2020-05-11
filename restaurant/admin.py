from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group


from .models import Menu, MenuItem, Location

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Location)
admin.site.unregister(Group)