# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stratosource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplateFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'email_template_folder',
            },
        ),
        migrations.AlterField(
            model_name='adminmessage',
            name='event_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='branch',
            name='cron_interval',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='branch',
            name='cron_start',
            field=models.CharField(default=b'10', max_length=5),
        ),
        migrations.AlterField(
            model_name='branchstats',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commit',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deploymentpackage',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deploymentpushstatus',
            name='date_attempted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='repo',
            name='location',
            field=models.CharField(blank=True, default=b'/var/sfrepo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='salesforceuser',
            name='lastActive',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='unittestbatch',
            name='batch_time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='emailtemplatefolder',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stratosource.Branch'),
        ),
    ]