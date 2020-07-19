# Generated by Django 3.0.8 on 2020-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_news_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='head',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='head_desc',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='keyword',
            field=models.CharField(max_length=60),
        ),
    ]
