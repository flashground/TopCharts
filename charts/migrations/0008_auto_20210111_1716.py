# Generated by Django 3.1.5 on 2021-01-11 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0007_auto_20210111_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='logo',
            new_name='logo_path',
        ),
    ]
