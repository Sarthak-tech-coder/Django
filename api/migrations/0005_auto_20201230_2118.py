# Generated by Django 3.1.4 on 2020-12-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_country_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
