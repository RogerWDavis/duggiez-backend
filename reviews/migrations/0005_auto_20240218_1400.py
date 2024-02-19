# Generated by Django 3.2.23 on 2024-02-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20240216_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AddField(
            model_name='review',
            name='profile_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
