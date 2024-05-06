from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'email_validated', 'phone_number',
                    'phone_number_validated']
    list_filter = ['first_name', 'last_name', 'email', 'email_validated', 'phone_number',
                   'phone_number_validated']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    ordering = ['id', 'email_validated','phone_number_validated']
