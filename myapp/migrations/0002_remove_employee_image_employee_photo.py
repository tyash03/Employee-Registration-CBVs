# Generated by Django 5.2.4 on 2025-07-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
