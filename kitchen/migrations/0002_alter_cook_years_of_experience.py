# Generated by Django 5.0 on 2024-01-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='years_of_experience',
            field=models.CharField(max_length=63),
        ),
    ]
