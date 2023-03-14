# Generated by Django 2.1.5 on 2023-03-14 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='club',
        ),
        migrations.RemoveField(
            model_name='approval',
            name='user',
        ),
        migrations.RemoveField(
            model_name='club',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='club',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='club',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Approval',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
