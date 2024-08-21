from django.contrib import admin
from Person_responsible_for_the_project.models import db_create_activity, db_activity_adduser

# Register your models here.

class DbCreateActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_name', 'activity_type', 'start_date_create_activity', 'due_date_create_activity', 'target_number', 'place', 'start_date_activity', 'due_date_activity', 'person_responsible_project', 'project_consultant', 'description', 'credit')

admin.site.register(db_create_activity, DbCreateActivityAdmin)
# db_activity_adduser
class db_activity_adduserAdmin(admin.ModelAdmin):
    list_display = ('student', 'activity_id', 'status')

admin.site.register(db_activity_adduser, db_activity_adduserAdmin)