# Generated by Django 2.2 on 2020-08-25 16:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_to_do_list_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=3000, null=True, validators=[webapp.models.at_least_10], verbose_name='Описание подробное:'),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='issue',
            field=models.ManyToManyField(related_name='issueses', to='webapp.Issues', verbose_name='Тип задачи:'),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='webapp.Project', verbose_name='Название проекта:'),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='webapp.Statuses', verbose_name='Статус:'),
        ),
        migrations.AlterField(
            model_name='to_do_list',
            name='summary',
            field=models.TextField(max_length=3000, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Описание:'),
        ),
    ]