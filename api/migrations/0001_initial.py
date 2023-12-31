# Generated by Django 4.2.3 on 2023-07-15 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('level', models.CharField(blank=True, choices=[('BASIC', '初階'), ('INTERMEDIATE', '中階'), ('ADVANCED', '進階')], max_length=15)),
                ('type', models.IntegerField(blank=True, choices=[(0, '帽子/伏地挺身'), (1, '手套/二頭彎舉'), (2, '鞋子/深蹲')])),
                ('color', models.CharField(blank=True, choices=[('DARK', '暗色'), ('BRIGHT', '亮色'), ('COLORFUL', '彩色')], max_length=255)),
                ('work_max', models.IntegerField(blank=True, null=True)),
                ('exp', models.FloatField(blank=True, default=0)),
                ('lucky', models.FloatField(blank=True, null=True)),
                ('coupon', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gear',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('accuracy', models.FloatField()),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gear')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'exercise',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('BASIC', '初級小物'), ('INTERMEDIATE', '中級小物'), ('HIGH_END', '高級小物')], max_length=255)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'thing',
                'managed': True,
                'unique_together': {('user', 'level')},
            },
        ),
    ]
