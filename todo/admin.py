from django.contrib import admin
from.models import *




class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'created_at', 'updated_at','completed', 'user')
  fields = ('title', 'description', 'user')
  search_fields = ('title', 'description', 'user')
  
  
  
# Register your models here.
admin.site.register(Todo, TodoAdmin)