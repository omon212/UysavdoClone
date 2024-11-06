from django.contrib import admin
from .models import UsersModel
# Register your models here.



@admin.register(UsersModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']