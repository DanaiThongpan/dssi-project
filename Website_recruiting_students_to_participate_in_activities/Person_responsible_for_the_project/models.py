from django.db import models
from Accounts.models import UserStudent, User

# Create your models here.
class db_create_activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_activity2')
    img_activity = models.ImageField(upload_to='media/activity/', blank=True, null=True)
    activity_name = models.CharField(max_length=30)
    activity_type_choices = [
        ('1 ด้านวิชาการที่ส่งเสริมคุณลักษณะบัณฑิตที่พึงประสงค์', '1 ด้านวิชาการที่ส่งเสริมคุณลักษณะบัณฑิตที่พึงประสงค์'),
        ('2 ด้านกีฬาหรือการส่งเสริมสุขภาพ', '2 ด้านกีฬาหรือการส่งเสริมสุขภาพ'),
        ('3 ด้านบำเพ็ญประโยชน์หรือรักษาสิ่งแวดล้อม', '3 ด้านบำเพ็ญประโยชน์หรือรักษาสิ่งแวดล้อม'),
        ('4 ด้านเสริมสร้างคุณธรรมและจริยธรรม', '4 ด้านเสริมสร้างคุณธรรมและจริยธรรม'),
        ('5 ด้านส่งเสริมศิลปะและวัฒนธรรม', '5 ด้านส่งเสริมศิลปะและวัฒนธรรม'),
        ('6 ด้านกิจกรรมอื่นๆ', '6 ด้านกิจกรรมอื่นๆ'),
    ]
    activity_type = models.CharField(max_length=100, choices=activity_type_choices)
    start_date_create_activity = models.DateTimeField()
    due_date_create_activity = models.DateTimeField()
    target_number = models.IntegerField(default=0)
    place = models.CharField(max_length=30)
    start_date_activity = models.DateTimeField()
    due_date_activity = models.DateTimeField()
    person_responsible_project = models.CharField(max_length=30)
    project_consultant = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    credit = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.id} {self.img_activity} {self.activity_name} {self.activity_type} {self.start_date_create_activity} {self.due_date_create_activity} {self.target_number} {self.place} {self.start_date_activity} {self.due_date_activity} {self.start_date_activity} {self.person_responsible_project} {self.project_consultant} {self.description}'

class db_activity_adduser(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='db_activity_adduser2')
    activity = models.ForeignKey(db_create_activity, on_delete=models.CASCADE, related_name='db_activity_adduser2')
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.status}'
    