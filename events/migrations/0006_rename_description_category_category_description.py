# Generated by Django 5.2 on 2025-04-15 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_name_event_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='category_description',
        ),
    ]
