# Generated by Django 5.0.1 on 2024-03-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gameapp', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
