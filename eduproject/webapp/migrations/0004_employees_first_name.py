# Generated by Django 2.0.2 on 2018-03-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_employees_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='first_name',
            field=models.CharField(default='kuldeep', max_length=10),
        ),
    ]