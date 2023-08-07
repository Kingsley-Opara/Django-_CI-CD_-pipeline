from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminChangeForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = Users
    search_fields = ['username', 'email', 'created']
    ordering = ['created', 'email']
    list_display = ['username', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    form = AdminChangeForm

    fieldsets = (
        (None, {'fields': (['username'])}),
        ('Personal info', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(Users, UserAdmin)
