"""
Created on May 22, 2017

@author: rafaelxy
"""
from __future__ import unicode_literals
from django.db import models
from django.db.models.query_utils import Q

class User(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(db_column='full name', max_length=200)  # Field renamed to remove unsuitable characters.
    age = models.IntegerField()

    class Meta:
        db_table = 'user'

class Conversation(models.Model):
    creator = models.ForeignKey('User', blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    message_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'conversation'

class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    sender = models.ForeignKey('User', related_name='sender', db_column='sender', blank=True, null=True)
    receiver = models.ForeignKey('User', related_name='receiver', db_column='receiver', blank=True, null=True)
    conversation = models.ForeignKey(Conversation, related_name='messages', blank=True, null=True)

    class Meta:
        db_table = 'message'
        ordering = ['-created_at']

    def is_invalid(self):
        """
        Checks if there is a user outside of the conversation trying to insert a message
        """
        sender_and_receiver_are_in = self.conversation.messages.filter(
            (Q(sender=self.sender) |
             Q(receiver=self.sender)) &
            (Q(sender=self.receiver) |
             Q(receiver=self.receiver)))

        if sender_and_receiver_are_in or self.conversation.messages.count() == 0:
            return False
        else:
            return { "error": "Either the sender or receiver are invalid for this conversation" }




