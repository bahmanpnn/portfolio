# Generated by Django 4.1.5 on 2023-01-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_user_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='langueges',
            name='grade',
            field=models.CharField(choices=[('available', 'Available to borrow'), ('borrowed', 'Borrowed by someone'), ('archived', 'Archived - not available anymore')], max_length=32, null=True),
        ),
    ]
