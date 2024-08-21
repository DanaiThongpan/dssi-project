# Generated by Django 5.0.3 on 2024-08-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_user_faculty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_of_credits_available',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='number_of_credits_required',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='type_Scholarship_or_Student_loan_fund',
            field=models.CharField(choices=[('ทุน', 'ทุน'), ('กยศ', 'กยศ'), ('ทุน, กยศ', 'ทุน, กยศ')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
