# Generated by Django 4.2.3 on 2023-08-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_gear_lucky'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='custom',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gear',
            name='coupon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
