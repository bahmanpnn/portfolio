# Generated by Django 4.1.5 on 2023-01-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_rename_linkdin_user_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='degrees',
            name='education_degree',
            field=models.CharField(max_length=150, null=True),
        ),
    ]