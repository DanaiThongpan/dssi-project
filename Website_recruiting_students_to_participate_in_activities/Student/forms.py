from django import forms
from django.db import models
from Accounts.forms import UserStudentrRegistrationForm
from Accounts.models import User, UserStudent
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your models here.
class UserStudentrUpdateForm(UserChangeForm):
    title = forms.ChoiceField(choices=UserStudent.title__choices, label='คำนำหน้า')
    faculty = forms.ChoiceField(choices=UserStudent.faculty_choices, label='คณะ')
    number_of_credits_required = forms.IntegerField(label='จำนวนหน่วยกิตที่ต้องการ')
    number_of_credits_available = forms.IntegerField(label='จำนวนหน่วยกิตที่มี')
    type_Scholarship_or_Student_loan_fund = forms.ChoiceField(choices=UserStudent.type_Scholarship_or_Student_loan_fund__choices, label='ประเภท(ทุน-กยศ)')
    class Meta:
        model = User
        fields = [
            'username',
            'title', 
            'first_name', 
            'last_name', 
            'email', 
            'faculty', 
            'number_of_credits_required',
            'number_of_credits_available',
            'type_Scholarship_or_Student_loan_fund',
        ]
        labels = {            
            'username' : 'รหัสนักศึกษา',
            'first_name' : 'ชื่อ',
            'last_name' : 'นามสกุล',
            'email' : 'อีเมล',
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_student, created = UserStudent.objects.get_or_create(user=user)
            if not created:
                user_student.title = self.cleaned_data['title']
                user_student.faculty = self.cleaned_data['faculty']
                user_student.first_name = self.cleaned_data['first_name']
                user_student.last_name = self.cleaned_data['last_name']
                user_student.email = self.cleaned_data['email']
                user_student.number_of_credits_required = self.cleaned_data['number_of_credits_required']
                user_student.number_of_credits_available = self.cleaned_data['number_of_credits_available']
                user_student.type_Scholarship_or_Student_loan_fund = self.cleaned_data['type_Scholarship_or_Student_loan_fund']
                user_student.save()
        return user