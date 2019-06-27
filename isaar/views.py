from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from clockwork_api.mixins.method_serializer_mixin import MethodSerializerMixin
from isaar.models import Isaar
from isaar.serializers import IsaarSelectSerializer, IsaarReadSerializer, IsaarWriteSerializer


class IsaarList(MethodSerializerMixin, generics.ListCreateAPIView):
    queryset = Isaar.objects.all()
    method_serializer_classes = {
        ('GET', ): IsaarReadSerializer,
        ('POST', ): IsaarWriteSerializer
    }


class IsaarDetail(MethodSerializerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Isaar.objects.all()
    method_serializer_classes = {
        ('GET', ): IsaarReadSerializer,
        ('PUT', 'PATCH', 'DELETE'): IsaarWriteSerializer
    }


class IsaarSelectList(generics.ListAPIView):
    serializer_class = IsaarSelectSerializer
    pagination_class = None
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('type',)
    search_fields = ('name',)
    queryset = Isaar.objects.all().order_by('name')