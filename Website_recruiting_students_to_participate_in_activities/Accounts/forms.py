from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import UserStudent, UserPerson_responsible_for_the_project, User

class UserStudentrRegistrationForm(UserCreationForm):
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
            'password1', 
            'password2'
        ]
        labels = {            
            'username' : 'รหัสนักศึกษา',
            'first_name' : 'ชื่อ',
            'last_name' : 'นามสกุล',
            'email' : 'อีเมล',
            'password1' : 'รหัสผ่าน',
            'password2' : 'ยืนยันรหัสผ่าน',
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserStudent.objects.create(
                # id=UserStudent.id,
                user=user, 
                title=self.cleaned_data['title'], 
                faculty=self.cleaned_data['faculty'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                number_of_credits_required=self.cleaned_data['number_of_credits_required'],
                number_of_credits_available=self.cleaned_data['number_of_credits_available'],
                type_Scholarship_or_Student_loan_fund=self.cleaned_data['type_Scholarship_or_Student_loan_fund'],
                )
        return user

class UserRegisterPerson_responsible_for_the_projectRegistrationForm(UserCreationForm):
    title = forms.ChoiceField(choices=UserPerson_responsible_for_the_project.title__choices, label='คำนำหน้า')
    faculty = forms.ChoiceField(choices=UserPerson_responsible_for_the_project.faculty_choices, label='คณะ')
    class Meta:
        model = User
        fields = [
            'username', 
            'title', 
            'first_name', 
            'last_name', 
            'email', 
            'faculty', 
            'password1', 
            'password2'
        ]
        labels = {            
            'username' : 'ชื่อผู้ใช้งาน',
            'title' : 'คำนำหน้า',
            'first_name' : 'ชื่อ',
            'last_name' : 'นามสกุล',
            'email' : 'อีเมล',
            'faculty' : 'คณะต้นสังกัด',
            'password1' : 'รหัสผ่าน',
            'password2' : 'ยืนยันรหัสผ่าน',
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserPerson_responsible_for_the_project.objects.create(
                user=user, 
                title=self.cleaned_data['title'], 
                faculty=self.cleaned_data['faculty'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                )
        return user