# Generated by Django 5.0.1 on 2024-01-31 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_completed_task_priority_alter_task_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 1, 31, 9, 57, 36, 936914, tzinfo=datetime.timezone.utc)),
        ),
    ]