# Generated by Django 2.2 on 2020-07-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200724_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='long_description',
            field=models.TextField(blank=True, default=None, max_length=3000, null=True, verbose_name='Описание'),
        ),
    ]
