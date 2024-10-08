# Generated by Django 5.0.3 on 2024-08-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_userstudent_type_scholarship_or_student_loan_fund'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.CharField(choices=[('วิทยาศาสตร์', 'วิทยาศาสตร์'), ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'), ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'), ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'), ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'), ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'), ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'), ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'), ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'), ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์')], default='วิทยาศาสตร์', max_length=50),
        ),
        migrations.AlterField(
            model_name='userstudent',
            name='type_Scholarship_or_Student_loan_fund',
            field=models.CharField(choices=[('ทุน', 'ทุน'), ('กยศ', 'กยศ'), ('ทุน, กยศ', 'ทุน, กยศ')], max_length=50),
        ),
    ]
