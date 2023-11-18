from django.contrib import admin
from .models import User, Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)

class UserAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'verified']
    list_editable = ['verified']
