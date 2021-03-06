# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-24 03:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('test100', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('itemtype', models.CharField(choices=[('Book', 'Book'), ('DVD', 'DVD'), ('Other', 'Other')], default='Other', max_length=6)),
                ('checked_out', models.BooleanField(default=False)),
                ('duedate', models.DateField(blank=True, default=None, null=True)),
                ('last_chkout', models.DateField(blank=True, default=None, null=True)),
                ('date_acquired', models.DateField(default=datetime.date(2016, 8, 23))),
                ('pubyr', models.IntegerField()),
                ('num_chkout', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Libuser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(default='Windsor', max_length=20)),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec')], default='ON', max_length=2)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=6, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pubyr', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Book', 'Book'), ('DVD', 'DVD'), ('Other', 'Other')], default='Other', max_length=6)),
                ('cost', models.IntegerField()),
                ('num_interested', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='testing',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test100.Libitem')),
                ('author', models.CharField(max_length=100)),
                ('category', models.IntegerField(choices=[(1, 'Fiction'), (2, 'Biography'), (3, 'Self Help'), (4, 'Education'), (5, 'Children'), (6, 'Teen'), (7, 'Other')], default=1)),
                ('barcodeimg', models.IntegerField()),
            ],
            bases=('test100.libitem',),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test100.Libitem')),
                ('maker', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField(choices=[(1, 'G'), (2, 'PG'), (3, 'PG-13'), (4, '14A'), (5, 'R'), (6, 'NR')], default=1)),
            ],
            bases=('test100.libitem',),
        ),
        migrations.AddField(
            model_name='libitem',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='test100.Libuser'),
        ),
    ]
