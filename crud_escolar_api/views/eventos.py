from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from crud_escolar_api.serializers import *
from crud_escolar_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json



class EventosView(generics.CreateAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "GET no implementado"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            evento = evento.objects.create(
                titulo=request.data['titulo'],
                tipo_de_evento=request.data['tipo_de_evento'],
                fecha_de_realizacion=request.data['fecha_de_realizacion'],
                hora_inicio=request.data['hora_inicio'],
                hora_fin=request.data['hora_fin'],
                lugar=request.data['lugar'],
                programa_educativo=request.data['programa_educativo'],
                responsable_del_evento=request.data['responsable_del_evento'],
                descripcion_breve=request.data['descripcion_breve'],
                cupo_max=request.data['cupo_max'],
                dias_json=json.dumps(request.data.get("dias_json", []))
            )
            evento.save()
            return Response({"Eventos_created_id": evento.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
