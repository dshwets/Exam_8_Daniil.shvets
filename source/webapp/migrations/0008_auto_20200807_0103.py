# Generated by Django 2.2 on 2020-08-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200807_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='webapp.Statuses', verbose_name='Статус'),
        ),
    ]