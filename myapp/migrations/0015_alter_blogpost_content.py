# Generated by Django 4.2 on 2025-05-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_yourmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(default=False),
        ),
    ]
