# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custorder',
            fields=[
                ('orderId', models.AutoField(serialize=False, primary_key=True, db_column='orderId')),
                ('orderNum', models.CharField(max_length=50, db_column='orderNum')),
                ('orderDate', models.DateTimeField(db_column='orderDate')),
                ('orderForDate', models.DateTimeField(db_column='orderForDate')),
                ('orderLogEmployee', models.SmallIntegerField(db_column='orderLogEmployee')),
                ('orderDiscount', models.FloatField(db_column='orderDiscount')),
            ],
            options={
                'db_table': 'custorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.AutoField(serialize=False, primary_key=True, db_column='itemId')),
                ('itemName', models.CharField(unique=True, max_length=50, db_column='itemName')),
                ('itemPrice', models.FloatField(null=True, db_column='itemPrice', blank=True)),
            ],
            options={
                'db_table': 'item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemQtyUnit',
            fields=[
                ('itemQtyUnitId', models.SmallIntegerField(serialize=False, primary_key=True, db_column='itemQtyUnitId')),
            ],
            options={
                'db_table': 'itemqtyunit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('orderItemsId', models.AutoField(serialize=False, primary_key=True, db_column='orderItemsId')),
                ('qty', models.SmallIntegerField()),
                ('orderItemPrice', models.FloatField(db_column='orderItemPrice')),
            ],
            options={
                'db_table': 'orderitems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QtyUnit',
            fields=[
                ('qtyUnitId', models.SmallIntegerField(serialize=False, primary_key=True, db_column='qtyUnitId')),
                ('qtyUnitName', models.CharField(unique=True, max_length=50, db_column='qtyUnitName')),
            ],
            options={
                'db_table': 'qtyunit',
                'managed': False,
            },
        ),
    ]
