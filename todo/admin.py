from django.contrib import admin
from.models import *




class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'created_at', 'updated_at','completed', 'user')
  fields = ('title', 'description', 'user')
  search_fields = ('title', 'description', 'user')
  
class KonnektorAdmin(admin.ModelAdmin):
  list_display = ('k_id', 'k_name')
  fields = ('k_id', 'k_name', 'k_is_active', 'k_online_since', 'k_firmware_version', 'k_update_available')
  search_fields = ('k_id', 'k_name', 'k_is_active', 'k_online_since', 'k_firmware_version', 'k_update_available')
  
# Register your models here.
admin.site.register(Todo, TodoAdmin)
admin.site.register(Konnektor, KonnektorAdmin)