# Generated by Django 5.2.4 on 2025-07-13 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
    ]
