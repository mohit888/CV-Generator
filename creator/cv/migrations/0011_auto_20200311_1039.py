# Generated by Django 3.0.2 on 2020-03-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20200310_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=129, primary_key=True, serialize=False, unique=True),
        ),
    ]