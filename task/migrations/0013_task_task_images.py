# Generated by Django 5.0.1 on 2024-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_task_image_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_images',
            field=models.ImageField(blank=True, null=True, upload_to='task_images/'),
        ),
    ]
