from django import forms
# from django.db import models
# from Accounts.forms import UserStudentrRegistrationForm
from Accounts.models import User, UserPerson_responsible_for_the_project
from django.contrib.auth.forms import UserChangeForm

# Create your models here.
class UserPerson_responsible_for_the_projectUpdateForm(UserChangeForm):
    title = forms.ChoiceField(choices=UserPerson_responsible_for_the_project.title__choices)
    faculty = forms.ChoiceField(choices=UserPerson_responsible_for_the_project.faculty_choices)
    class Meta:
        model = User
        fields = [
            'username',
            'title', 
            'first_name', 
            'last_name', 
            'email', 
            'faculty', 
        ]
        labels = {            
            'username' : 'ชื่อผู้ใช้งาน',
            'title' : 'คำนำหน้า',
            'first_name' : 'ชื่อ',
            'last_name' : 'นามสกุล',
            'email' : 'อีเมล',
            'faculty' : 'คณะ',
            'password1' : 'รหัสผ่าน',
            'password2' : 'ยืนยันรหัสผ่าน',
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_student, created = UserPerson_responsible_for_the_project.objects.get_or_create(user=user)
            if not created:
                user_student.title = self.cleaned_data['title']
                user_student.faculty = self.cleaned_data['faculty']
                user_student.first_name = self.cleaned_data['first_name']
                user_student.last_name = self.cleaned_data['last_name']
                user_student.email = self.cleaned_data['email']
                user_student.save()
        return user
    
from Person_responsible_for_the_project.models import db_create_activity

class forms_create_activity(forms.ModelForm):
    class Meta:
        model = db_create_activity
        fields = [
            # 'user',
            'img_activity',
            'activity_name',
            'activity_type',
            'start_date_create_activity',
            'due_date_create_activity',
            'target_number',
            'place',
            'start_date_activity',
            'due_date_activity',
            'person_responsible_project',
            'project_consultant',
            'description',
            'credit',
        ]
        
        # exclude = ['user']

        labels = {
            'img_activity' : 'รูปกิจกรรม ',
            'activity_name' : 'ชื่อกิจกรรม ',
            'activity_type' : 'ด้านที่ ',
            'start_date_create_activity' : 'วันที่เปิดรับสมัคร ',
            'due_date_create_activity' : 'วันที่ปิดรับสมัคร ',
            'target_number' : 'จำนวนเป้าหมาย ',
            'place' : 'สถานที่จัดกิจกรรม ',
            'start_date_activity' : 'วันที่จัดกิจกรรม ',
            'due_date_activity' : 'วันที่สิ้นสุดกิจกรรม ',
            'person_responsible_project' : 'ผู้รับผิดชอบโครงการ ',
            'project_consultant' : 'ที่ปรึกษาโครงการ ',
            'description' : 'คำอธิบาย ',
            'credit' : 'หน่วยกิจกรรม',
        }
