# Generated by Django 3.0.8 on 2020-07-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20200713_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
