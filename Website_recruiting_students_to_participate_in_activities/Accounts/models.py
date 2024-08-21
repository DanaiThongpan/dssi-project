from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import User

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_person_responsible_for_the_project = models.BooleanField(default=False)
    faculty_choices = [
        ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
        ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'),
        ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'),
        ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'),
        ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'),
        ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'),
        ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'),
        ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'),
        ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'),
        ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์'),
    ]
    faculty = models.CharField(max_length=50, choices=faculty_choices, default="วิทยาศาสตร์")
    #Student

class UserStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentprofile')
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='user_student_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='user_student_user_permissions')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    type_Scholarship_or_Student_loan_fund__choices = [
        ('ทุน', 'ทุน'),
        ('กยศ', 'กยศ'),
        ('ทุน, กยศ', 'ทุน, กยศ'),
    ]
    type_Scholarship_or_Student_loan_fund = models.CharField(max_length=50, choices=type_Scholarship_or_Student_loan_fund__choices)
    number_of_credits_required = models.IntegerField()
    number_of_credits_available = models.IntegerField()
    email = models.EmailField()
    title__choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
        ('นาง', 'นาง'),
    ]
    title = models.CharField(max_length=10, choices=title__choices, default="นาย")
    faculty_choices = [
        ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
        ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'),
        ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'),
        ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'),
        ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'),
        ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'),
        ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'),
        ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'),
        ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'),
        ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์'),
    ]
    faculty = models.CharField(max_length=50, choices=faculty_choices, default="วิทยาศาสตร์")
    def __str__(self) -> str:
        return (f'{self.user, self.faculty, self.first_name, self.last_name, self.email, self.title }')
    
class UserPerson_responsible_for_the_project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person_responsible_for_the_projectprofile')
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='user_person_responsible_for_the_project_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='user_person_responsible_for_the_project_user_permissions')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    title__choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
        ('นาง', 'นาง'),
    ]
    title = models.CharField(max_length=10, choices=title__choices, default="นาย")
    faculty_choices = [
        ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
        ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'),
        ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'),
        ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'),
        ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'),
        ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'),
        ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'),
        ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'),
        ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'),
        ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์'),
    ]
    faculty = models.CharField(max_length=50, choices=faculty_choices, default="วิทยาศาสตร์")
