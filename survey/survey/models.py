# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    identify = models.CharField(max_length=20, blank=True, null=True)
    qid = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='qid', blank=True, null=True)
    pid = models.ForeignKey('Paper', on_delete=models.CASCADE, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class Entrust(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    pid = models.ForeignKey('Paper', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrust'


class Filelist(models.Model):
    info = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    pid = models.ForeignKey('Paper', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filelist'


class Limitnumber(models.Model):
    type = models.CharField(max_length=7, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limitnumber'


class Limittime(models.Model):
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limittime'


class Option(models.Model):
    no = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    qid = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='qid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option'


class Paper(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    url = models.CharField(max_length=20, blank=True, null=True)
    verify = models.CharField(max_length=20, blank=True, null=True)
    uid = models.ForeignKey('User', db_column='uid', blank=True, null=True,on_delete=models.CASCADE)
    timelimit = models.ForeignKey(Limittime,  db_column='timelimit', blank=True, null=True,on_delete=models.CASCADE)
    numberlimit = models.ForeignKey(Limitnumber,  db_column='numberlimit', blank=True, null=True,on_delete=models.CASCADE)
    islist = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper'


class Question(models.Model):
    no = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    ismustfill = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    pid = models.ForeignKey(Paper, on_delete=models.CASCADE, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email=models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'user'
