# Generated by Django 5.0.1 on 2024-01-31 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 1, 31, 10, 11, 59, 137598, tzinfo=datetime.timezone.utc)),
        ),
    ]
