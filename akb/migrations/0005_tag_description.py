# Generated by Django 2.2.12 on 2020-07-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akb', '0004_tag_priority_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]