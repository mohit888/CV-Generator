# Generated by Django 3.0.2 on 2020-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200309_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=6, primary_key=True, serialize=False, unique=True),
        ),
    ]