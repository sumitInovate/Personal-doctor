# Generated by Django 3.0.3 on 2020-03-12 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personaldoc', '0011_patients_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='profile_pic',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='patients',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]