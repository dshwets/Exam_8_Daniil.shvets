# Generated by Django 2.2 on 2020-09-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200926_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]
