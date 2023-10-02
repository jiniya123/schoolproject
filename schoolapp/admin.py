from django.contrib import admin
from .models import Department, Course, Material, UserProfile,Purpose

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(UserProfile)
admin.site.register(Purpose)
