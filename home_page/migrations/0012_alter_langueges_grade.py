# Generated by Django 4.1.5 on 2023-01-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_alter_langueges_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='langueges',
            name='grade',
            field=models.CharField(choices=[('elementry', 'elementry'), ('midLevel', 'midLevel'), ('professional', 'professional'), ('native', 'native')], max_length=32, null=True),
        ),
    ]