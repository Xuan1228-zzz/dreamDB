# Generated by Django 4.2.3 on 2023-07-25 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_gear_loaded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weektask',
            old_name='task_count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='weektask',
            old_name='last_completed_date',
            new_name='last_completed',
        ),
        migrations.RenameField(
            model_name='weektask',
            old_name='week_start_date',
            new_name='week_start',
        ),
    ]