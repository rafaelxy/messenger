"""
Created on May 22, 2017

@author: rafaelxy
"""
from django.db import transaction
from django.db.models.query_utils import Q
from messenger.models import Conversation, Message
from messenger.serlializers import ConversationSerializer, MessageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

class ConversationView(APIView):
    def get(self, request, user_id, conversation_id):
        """
        GET request that filters out messages that are either from the sender
        or the receiver
        """
        try:
            conversations = Conversation.find_by_user(conversation_id, user_id)
            serializer = ConversationSerializer(conversations, many=True)
            return Response({ "conversation": serializer.data })
        except Exception, e:
            return Response({ "error": str(e) }, status=status.HTTP_400_BAD_REQUEST)

class NewMessageView(APIView):
    @transaction.atomic
    def post(self, request, conversation_id):
        """
        POST request for creating new messages in a existing conversation
        """
        try:
            conversation = Conversation.objects.get(id=conversation_id)
            conversation.message_count += 1

            new_msg = Message(**request.data)
            new_msg.conversation = conversation
            new_msg.created_at = datetime.datetime.now()

            errors = new_msg.is_invalid()
            if not errors:
                new_msg.save()
                conversation.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            return Response({ "error": str(e) }, status=status.HTTP_400_BAD_REQUEST)


