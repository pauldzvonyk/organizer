# Generated by Django 5.0.1 on 2024-05-04 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0022_rename_subtask10_text_task_subtask_text_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.category'),
        ),
    ]