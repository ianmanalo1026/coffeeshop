from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    list_filter = ('email', 'user_name', 'first_name', 'last_name',
                   'is_active', 'is_staff')
    ordering = ('-creation_date',)
    list_display = ('email', 'user_name', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields':('email', 'user_name')}),
        ('Permission', {'fields':('is_active', 'is_staff')}),
        ('Personal', {'fields':('first_name','last_name','address', 'phone_number','gender')})
    )
    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields': ('email', 'user_name', 'first_name', 'last_name',
                       'password1','password2', 'address', 'phone_number', 'gender')
        }),
    )
admin.site.register(NewUser, UserAdminConfig)