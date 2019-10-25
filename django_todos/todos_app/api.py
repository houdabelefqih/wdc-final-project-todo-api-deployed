import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import *
from rest_framework.permissions import *

from todos_app.models import Todo
from todos_app.serializers import TodoModelSerializer


class BaseCSRFExemptView(viewsets.ModelViewSet):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TodoModelViewSet(BaseCSRFExemptView):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()

    # @action(detail=False, methods=['GET'], url_path='all-invoices')
    # def all_invoices(self, request, pk=None):
    #     return Response({"msg": "All invoices list!!!!"})
    #
    # @action(detail=True, methods=['GET'], url_path='detail-invoices')
    # def detail_invoices(self, request, pk=None):
    #     return Response({"msg": "Detail invoices {}!!!!".format(pk)})
    #
