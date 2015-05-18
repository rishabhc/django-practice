from django.contrib import admin
from .models import Subject
from .models import TimeTable

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('subject_name','classes_attended','classes_held','percentage_attendance','is_attendance_not_low')
	search_fields = ['subject_name']	
	list_filter = ['percentage_attendance']

class TimeTableAdmin(admin.ModelAdmin):
	list_display = TimeTable._meta.get_all_field_names()

admin.site.register(Subject,SubjectAdmin)
admin.site.register(TimeTable,TimeTableAdmin)