# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guratorapp', '0010_auto_20160510_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_creator', to='guratorapp.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='GroupParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guratorapp.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guratorapp.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(through='guratorapp.GroupParticipant', to='guratorapp.Participant'),
        ),
    ]
