# Generated by Django 3.2.12 on 2022-03-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_article_is_married'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(default=False, max_length=20),
            preserve_default=False,
        ),
    ]