# Generated by Django 5.1.1 on 2025-04-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feature_details_feature_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feature',
        ),
    ]
