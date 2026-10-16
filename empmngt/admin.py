from django.contrib import admin
from empmngt.models import Calender, Employee, News, Job

# Register your models here.

class CalenderAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Occasion')
admin.site.register(Calender, CalenderAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('Details',)
admin.site.register(News, NewsAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Emp_ID', 'Department')
admin.site.register(Employee, EmployeeAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('Role', 'Experience', 'Skills')
admin.site.register(Job, JobAdmin)

