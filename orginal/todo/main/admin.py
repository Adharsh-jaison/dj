from django.contrib import admin
from . models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    last_display="firstname","lastname","country"



admin.site.register(Member,MemberAdmin)