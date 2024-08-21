from django.contrib import admin
from Accounts.models import UserStudent, UserPerson_responsible_for_the_project, User

# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display = ['username', 
                    'email', 
                    'faculty', 
                    'first_name', 
                    'last_name', 
                    'is_staff', 
                    'is_student', 
                    'is_person_responsible_for_the_project']

admin.site.register(User, 
                    UserDisplay,
                    )

# class UserStudentAdmin(admin.ModelAdmin):
#     list_display = ['faculty']
# @admin.register(UserStudent)
class UserStudentAdminDisplay(admin.ModelAdmin):
    list_display = [ 'user', 
                    'title', 
                    'first_name', 
                    'last_name', 
                    'email', 
                    'faculty', 
                    'type_Scholarship_or_Student_loan_fund', 
                    'number_of_credits_required', 
                    'number_of_credits_available']

admin.site.register(UserStudent, 
                    UserStudentAdminDisplay,
                    )

class UserPerson_responsible_for_the_projectAdminDisplay(admin.ModelAdmin):
    list_display = [ 'user', 'title', 'first_name', 'last_name', 'email', 'faculty']

admin.site.register(UserPerson_responsible_for_the_project, 
                    UserPerson_responsible_for_the_projectAdminDisplay,
                    )