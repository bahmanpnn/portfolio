# Generated by Django 4.1.5 on 2023-01-09 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_rename_whatsup_user_whatsapp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='linkdin',
            new_name='linkedin',
        ),
    ]
