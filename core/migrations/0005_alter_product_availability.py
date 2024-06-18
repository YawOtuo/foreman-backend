# Generated by Django 5.0.6 on 2024-06-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_uid_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('pending', 'Pending')], default='available', max_length=50),
        ),
    ]
