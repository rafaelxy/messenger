"""
Created on May 22, 2017

@author: rafaelxy
"""
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class User(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(db_column='full name', max_length=200)  # Field renamed to remove unsuitable characters.
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

class Conversation(models.Model):
    creator = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    message_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversation'

class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    sender = models.ForeignKey('User', models.DO_NOTHING, db_column='sender', blank=True, null=True)
    receiver = models.ForeignKey('User', models.DO_NOTHING, db_column='receiver', blank=True, null=True)
    conversation = models.ForeignKey(Conversation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


