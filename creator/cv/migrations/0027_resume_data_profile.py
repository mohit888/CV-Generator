# Generated by Django 3.0.2 on 2020-04-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0026_auto_20200415_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_data',
            name='profile',
            field=models.TextField(default=' '),
        ),
    ]