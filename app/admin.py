from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(User)
@admin.register(User)
class customAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'email', 'contact']