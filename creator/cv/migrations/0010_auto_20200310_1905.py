# Generated by Django 3.0.2 on 2020-03-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20200310_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=75, primary_key=True, serialize=False, unique=True),
        ),
    ]