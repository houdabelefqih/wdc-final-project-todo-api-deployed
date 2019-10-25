
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework.permissions import *

from todos_app.models import Todo
from todos_app.serializers import TodoModelSerializer


class BaseCSRFExemptView(viewsets.ModelViewSet):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TodoModelViewSet(BaseCSRFExemptView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
