# Generated by Django 5.1.3 on 2024-11-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
