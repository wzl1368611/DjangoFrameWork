# Generated by Django 2.1.8 on 2019-08-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_article_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0),
        ),
    ]