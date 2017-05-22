"""
Created on May 22, 2017

@author: rafaelxy
"""
from django.db.models.query_utils import Q
from messenger.models import Conversation
from messenger.serlializers import ConversationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ConversationView(APIView):
    def get(self, request, user_id, conversation_id):
        """
        GET that filters out messages that are either from the sender or the receiver
        """

        conversations = Conversation.objects.filter(
            Q(id=conversation_id) &
                (Q(messages__sender=user_id) |
                 Q(messages__receiver=user_id))).distinct()

        serializer = ConversationSerializer(conversations, many=True)
        return Response({ "conversation": serializer.data })
