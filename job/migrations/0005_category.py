# Generated by Django 5.2.4 on 2025-07-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_experience_job_published_at_job_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
