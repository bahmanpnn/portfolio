# Generated by Django 4.1.5 on 2023-01-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_user_nationality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='whatsup',
            new_name='whatsapp',
        ),
    ]
