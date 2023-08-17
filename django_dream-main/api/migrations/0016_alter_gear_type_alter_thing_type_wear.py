# Generated by Django 4.2.3 on 2023-08-07 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_email'),
        ('api', '0015_alter_thing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='type',
            field=models.CharField(choices=[('b1', 'Hair/B1'), ('b2', 'Hair/B2'), ('b3', 'Hair/B3'), ('g1', 'Hair/G1'), ('g2', 'Hair/G2'), ('g3', 'Hair/G3'), ('c1', 'Top/C1'), ('c2', 'Top/C2'), ('c3', 'Top/C3'), ('c4', 'Top/C4'), ('c5', 'Top/C5'), ('c6', 'Top/C6'), ('pb1', 'Bottom/Pb1'), ('pb2', 'Bottom/Pb2'), ('pb3', 'Bottom/Pb3'), ('pg1', 'Bottom/Pg1'), ('pg2', 'Bottom/Pg2'), ('pg3', 'Bottom/Pg3'), ('s1', 'Shoes/S1'), ('s2', 'Shoes/S2'), ('s3', 'Shoes/S3'), ('s4', 'Shoes/S4'), ('s5', 'Shoes/S5'), ('s6', 'Shoes/S6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='thing',
            name='type',
            field=models.CharField(choices=[('dumbbell', '初級小物/dumbbell'), ('energy_drink', '中級小物/energy_drink'), ('protein_powder', '高級小物/protein_powder')], default='dumbbell', max_length=20),
        ),
        migrations.CreateModel(
            name='Wear',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wear', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bottom', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bottom', to='api.gear')),
                ('hair', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hair', to='api.gear')),
                ('shoes', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='api.gear')),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='api.gear')),
                ('top', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top', to='api.gear')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
