# Generated by Django 3.1.5 on 2021-02-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210202_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Avatar'),
        ),
    ]
