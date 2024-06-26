# Generated by Django 5.0.3 on 2024-04-11 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_approvedelivery_paid'),
        ('post', '0007_remove_service_estimated_arrival_time_and_more'),
        ('user', '0007_serviceproviders_fayda_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedelivery',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_delivery', to='core.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='consumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_orders', to='user.profile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='post.service'),
        ),
    ]
