from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'name', 'email', 'last_login']
    search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)
