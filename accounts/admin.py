from django.contrib import admin
# to disable password to edit
from django.contrib.auth.admin import UserAdmin
from .models import Account

# to disable password edit in admin
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)
  
  #its make password read only  
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)
