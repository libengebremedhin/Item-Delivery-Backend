# Generated by Django 5.0.3 on 2024-04-15 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_rename_departur_time_path_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths', to='post.service'),
        ),
    ]
