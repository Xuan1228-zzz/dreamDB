# Generated by Django 4.2.3 on 2023-08-21 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_merge_20230819_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='video_url',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='img_url',
        ),
    ]