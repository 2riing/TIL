# Generated by Django 3.2.12 on 2022-03-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_married',
            field=models.BooleanField(default=False),
        ),
    ]
