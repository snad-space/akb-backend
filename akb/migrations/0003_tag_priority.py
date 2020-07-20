# Generated by Django 2.2.12 on 2020-07-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akb', '0002_object_simbadid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='tag',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['priority'], name='akb_tag_priorit_361b7a_idx'),
        ),
    ]
