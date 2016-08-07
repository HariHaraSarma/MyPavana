# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-05 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compltestockdetails',
            options={'verbose_name_plural': 'Stock Info'},
        ),
        migrations.AlterModelOptions(
            name='dealersinfo',
            options={'verbose_name_plural': 'Dealers Info'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'Person Info'},
        ),
        migrations.AlterField(
            model_name='compltestockdetails',
            name='batch_num',
            field=models.IntegerField(unique=True, verbose_name='batch No.'),
        ),
        migrations.AlterField(
            model_name='compltestockdetails',
            name='exp_date',
            field=models.CharField(max_length=10, verbose_name='expiry date'),
        ),
        migrations.AlterField(
            model_name='compltestockdetails',
            name='item_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='item name'),
        ),
        migrations.AlterField(
            model_name='compltestockdetails',
            name='manf_date',
            field=models.CharField(max_length=10, verbose_name='manufacturing date'),
        ),
        migrations.AlterField(
            model_name='compltestockdetails',
            name='price_per_unit',
            field=models.FloatField(verbose_name='price per unit'),
        ),
        migrations.AlterField(
            model_name='dealersinfo',
            name='dl1',
            field=models.CharField(max_length=15, unique=True, verbose_name='dealer 1'),
        ),
        migrations.AlterField(
            model_name='dealersinfo',
            name='dl2',
            field=models.CharField(max_length=15, unique=True, verbose_name='dealer 2'),
        ),
        migrations.AlterField(
            model_name='dealersinfo',
            name='tin',
            field=models.CharField(max_length=15, unique=True, verbose_name='tin number'),
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=10, unique=True, verbose_name='phone no.'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pwd',
            field=models.CharField(max_length=20, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.CharField(max_length=20, unique=True, verbose_name='user name'),
        ),
    ]