# Generated by Django 5.0.1 on 2024-02-14 05:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_task_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
