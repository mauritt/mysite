from django.contrib import admin
from .models import Video, Role, Company
# Register your models here.

class videoAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",)}

class roleAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",)}

class companyAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",)}



admin.site.register(Video, videoAdmin)
admin.site.register(Role, roleAdmin)
admin.site.register(Company, companyAdmin)
