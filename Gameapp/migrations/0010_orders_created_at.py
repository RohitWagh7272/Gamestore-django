# Generated by Django 5.0.3 on 2024-04-18 08:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gameapp', '0009_rename_order_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
