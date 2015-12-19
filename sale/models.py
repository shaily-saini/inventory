# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    itemid = models.SmallIntegerField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    itemuniquekey = models.CharField(db_column='ItemUniqueKey', unique=True, max_length=100)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=250)  # Field name made lowercase
    isvalid = models.BooleanField(db_column='isvalid', default=True)
    isavailable = models.BooleanField(db_column='isavailable', default=True)

    class Meta:
        managed = False
        db_table = 'item'

class Offer(models.Model):
    offerid = models.SmallIntegerField(db_column='offerId', primary_key=True)  # Field name made lowercase.
    discountrate = models.FloatField(db_column='discountRate')  # Field name made lowercase.
    offername = models.CharField(db_column='offerName', max_length=50)  # Field name made lowercase.
    validfrom = models.DateField(db_column='validFrom')  # Field name made lowercase.
    validtill = models.DateField(db_column='validTill')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offer'


class Offeritem(models.Model):
    offeritemid = models.SmallIntegerField(db_column='offerItemId', primary_key=True)  # Field name made lowercase.
    offerid = models.ForeignKey(Offer, db_column='offerId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, db_column='itemId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offeritem'


class Category(models.Model):
    categoryid = models.SmallIntegerField(db_column='categoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Custorder(models.Model):
    custorderid = models.AutoField(db_column='CustOrderId', primary_key=True)  # Field name made lowercase.
    custordernum = models.CharField(db_column='CustOrderNum', max_length=50)  # Field name made lowercase.
    custorderdate = models.DateTimeField(db_column='CustOrderDate')  # Field name made lowercase.
    orderfordate = models.DateTimeField(db_column='OrderForDate')  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True, db_column='discount')
    #tax = models.FloatField(blank=True, null=True, db_column='tax')
    originalamount = models.FloatField(db_column='originalamount')
    totalamount = models.FloatField(db_column='totalamount')

    class Meta:
        managed = False
        db_table = 'custorder'

class Measuringunit(models.Model):
    measuringunitid = models.SmallIntegerField(db_column='measuringUnitId', primary_key=True)  # Field name made lowercase.
    measuringunitname = models.CharField(db_column='measuringUnitName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measuringunit'


#this table is replica of order slip
class custOrderItems(models.Model):
    id = models.AutoField(db_column='custOrderItemsId', primary_key=True)
    custorderid = models.ForeignKey(Custorder, db_column='custorderid')
    itemid = models.ForeignKey(Item, db_column='itemid')
    qty = models.FloatField(db_column='qty')
    measuringunitid = models.ForeignKey(Measuringunit, db_column='measuringunitid')
    priceperunit = models.FloatField(db_column='pricePerUnit')
    offeridavailed = models.ForeignKey(Offeritem, db_column='offeridavailed')
    offerpriceperunit = models.FloatField(db_column='offerPricePerUnit')
    price = models.FloatField(db_column='price')

    class Meta:
        unique_together = (("custorderid", "itemid"),)
        managed = False
        db_table = 'custOrderItems'


class Itemcategory(models.Model):
    itemcategoryid = models.SmallIntegerField(db_column='itemCategoryId', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, db_column='categoryId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemcategory'


class Itemmeasuringunit(models.Model):
    itemmeasuringunitid = models.SmallIntegerField(db_column='itemMeasuringUnitId', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    measuringunitid = models.ForeignKey('Measuringunit', db_column='measuringUnitId', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='isValid', default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemmeasuringunit'


class Itempricechart(models.Model):
    itempricechartid = models.SmallIntegerField(db_column='itemPriceChartId', primary_key=True)  # Field name made lowercase.
    itemmeasuringunitid = models.ForeignKey(Itemmeasuringunit, db_column='itemMeasuringUnitId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField()
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'itempricechart'

