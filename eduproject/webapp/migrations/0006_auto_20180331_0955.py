# Generated by Django 2.0.2 on 2018-03-31 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20180331_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='slug',
            new_name='emp_slug',
        ),
    ]
