"""
Created on May 22, 2017

@author: rafaelxy
"""

from django.urls import reverse
from messenger.models import Conversation, Message, User
from rest_framework import status
from rest_framework.test import APITestCase
import datetime

class NewMessageTests(APITestCase):
    def setUp(self):
        self.user_a = User(
            username="user_a",
            full_name="User A",
            age=21,)
        self.user_a.save()

        self.user_b = User(
            username="user_b",
            full_name="User B",
            age=21,)
        self.user_b.save()

        self.user_c = User(
            username="user_c",
            full_name="User C",
            age=21,)
        self.user_c.save()

        self.conversation = Conversation(
            creator=self.user_a,
            create_at=datetime.datetime.now(),
            message_count=0,)
        self.conversation.save()

    def test_conversation_with_zero_messages(self):
        """
        Test if a plain conversation with zero messages can be started
        """
        response = self.client.post('/conversation/{}/message'.format(self.conversation.id), {
            "sender_id": self.user_a.id,
            "receiver_id": self.user_b.id,
            "text": "test message"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().text, 'test message')

#
    def test_user_not_in_conversation(self):
        """
        Test if a user outside a conversation can insert a message
        """
        self.client.post('/conversation/{}/message'.format(self.conversation.id), {
            "sender_id": self.user_a.id,
            "receiver_id": self.user_b.id,
            "text": "test message"
        }, format='json')
        response = self.client.post('/conversation/{}/message'.format(self.conversation.id), {
            "sender_id": self.user_a.id,
            "receiver_id": self.user_c.id,
            "text": "test message"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Message.objects.count(), 1)

#     def test_new_conversation(self):
#         pass
#     def test_user_not_exists(self):
#         pass
#     def test_conversation_does_not_exist(self):
#         pass


