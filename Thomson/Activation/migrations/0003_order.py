# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activation', '0002_customer_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('order_name', models.CharField(max_length=50)),
                ('order_quantity', models.IntegerField()),
                ('img', models.CharField(default='https://www.iconexperience.com/_img/g_collection_png/standard/512x512/purchase_order.png', max_length=2000)),
            ],
        ),
    ]
