# Generated by Django 5.1.7 on 2025-03-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obituaries', '0002_remove_obituary_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obituary',
            name='biography',
            field=models.TextField(default=''),
        ),
    ]
