# Generated by Django 4.2.2 on 2023-06-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('passward', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
