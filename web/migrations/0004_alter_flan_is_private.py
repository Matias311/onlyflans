# Generated by Django 5.1 on 2024-09-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
