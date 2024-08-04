from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'pfile']



admin.site.register(Profile, ProfileModelAdmin)