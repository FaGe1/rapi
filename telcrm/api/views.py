from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Tg_user.objects.all().order_by('id')
    serializer_class = Tg_userSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all().order_by('id')
    serializer_class = ConversationSerializer

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        user = queryset.filter(customer__id=pk)
        serializer = ConversationSerializer(user,many=True)
        return Response(serializer.data)

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('id')
    serializer_class = OfferSerializer

    def retrieve(self, request, pk=None):
        queryset = Offer.objects.all()
        user = queryset.filter(project__id=pk)
        serializer = OfferSerializer(user,many=True)
        return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        user = queryset.filter(offer__id=pk)
        serializer = TaskSerializer(user,many=True)
        return Response(serializer.data)

class PTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        user = queryset.filter(project__id=pk)
        serializer = TaskSerializer(user,many=True)
        return Response(serializer.data)

class DTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        user = queryset.filter(developer__id=pk)
        serializer = TaskSerializer(user,many=True)
        return Response(serializer.data)

class Month_TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        current_datetime = datetime.now()
        queryset = Task.objects.all()
        user = queryset.filter(
            created__year=current_datetime.year,
            created__month=current_datetime.month
        )
        serializer = TaskSerializer(user,many=True)
        return Response(serializer.data)
class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        queryset = Template.objects.all()
        text = queryset.filter(project__id=pk)
        serializer = TemplateSerializer(text,many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        user = queryset.filter(id=pk)
        serializer = EventSerializer(user,many=True)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer

    def retrieve(self, request, pk=None):
        queryset = Message.objects.all()
        text = queryset.filter(project__id=pk)
        serializer = MessageSerializer(text,many=True)
        return Response(serializer.data)

class ResenderViewSet(APIView):
    def get(self, request, pk=None):
        conv_dev = False
        conv_cus = False
        try:
            conv_dev = Conversation.objects.get(dev_chat_id=pk)
        except:
            pass
        try:
            conv_cus = Conversation.objects.get(cus_chat_id=pk)
        except:
            pass
        print(conv_cus)
        if conv_cus:
            return Response({'dev_id':conv_cus.dev_chat_id})
        elif conv_dev:
            return Response({'cus_id':conv_dev.cus_chat_id})
        else:
            return Response({})

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        text = queryset.filter(project__id=pk)
        serializer = ServiceSerializer(text,many=True)
        return Response(serializer.data)