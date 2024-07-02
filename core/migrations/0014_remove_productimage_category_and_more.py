# Generated by Django 5.0.6 on 2024-07-02 17:45

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_category_image_remove_productimage_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product_variant',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.productvariant'),
        ),
    ]
