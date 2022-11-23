from django.contrib import admin
from webapp.models import student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =['stdno', 'stdname', 'stdmarks', 'stdresult']
admin.site.register(student,StudentAdmin)