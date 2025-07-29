from django.contrib import admin
from Api.models import Company,Empolyee
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)   
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Empolyee,EmployeeAdmin)