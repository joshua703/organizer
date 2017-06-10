# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0006_auto_20170609_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.DateTimeField(blank=True, default=None)),
                ('opened', models.DateTimeField(blank=True, default=None)),
                ('bounced', models.BooleanField(default=False)),
                ('message_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TemplatedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='mailsubmission',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to='emails.TemplatedEmail'),
        ),
        migrations.AddField(
            model_name='mailsubmission',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_recipients', to='crm.Activist'),
        ),
    ]