"""
Created on May 22, 2017

@author: rafaelxy
"""
from messenger.models import Conversation, Message, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    def to_representation(self, obj):
        return obj.username

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'created_at', 'text')

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ('id', 'create_at', 'message_count', 'messages')



