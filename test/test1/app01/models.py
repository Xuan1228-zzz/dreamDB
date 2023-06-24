# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Eq(models.Model):
    nid = models.IntegerField(db_column='Nid', primary_key=True)  # Field name made lowercase.
    hash = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    work_max = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    lucky = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    coupon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq'


class Exercise(models.Model):
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=255, blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, timestamp) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'exercise'
        unique_together = (('user', 'timestamp'),)


class Thing(models.Model): #django的admin頁面名稱後面會加s
    type = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, type) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'things' #things MYSQL的TABKE_NAME
        unique_together = (('user', 'type'),)


class User(models.Model): #django的admin頁面名稱後面會加s
    uid = models.IntegerField(db_column='Uid', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    wallet_addr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users' #users MYSQL的TABKE_NAME
