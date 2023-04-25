from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','company']
    # raw_id_fields=['company']
admin.site.register(Company)