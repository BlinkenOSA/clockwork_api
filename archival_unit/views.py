from django.db.models.query_utils import Q
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from archival_unit.models import ArchivalUnit
from archival_unit.serializers import ArchivalUnitSelectSerializer, ArchivalUnitReadSerializer, \
    ArchivalUnitWriteSerializer, ArchivalUnitFondsSerializer, ArchivalUnitSeriesSerializer, \
    ArchivalUnitPreCreateSerializer
from clockwork_api.mixins.method_serializer_mixin import MethodSerializerMixin


class ArchivalUnitFilterClass(filters.FilterSet):
    search = filters.CharFilter(label='Search', method='search_filter')

    def search_filter(self, queryset, name, value):
        return ArchivalUnit.objects.filter(
            (
                Q(title__icontains=value) |
                Q(children__title__icontains=value) |
                Q(children__children__title__icontains=value)
            ) & Q(level='F')
        ).distinct()

    class Meta:
        model = ArchivalUnit
        fields = ('fonds',)


class ArchivalUnitPreCreate(generics.RetrieveAPIView):
    queryset = ArchivalUnit.objects.all()
    serializer_class = ArchivalUnitPreCreateSerializer


class ArchivalUnitList(MethodSerializerMixin, generics.ListCreateAPIView):
    queryset = ArchivalUnit.objects.filter(level='F')
    method_serializer_classes = {
        ('GET', ): ArchivalUnitFondsSerializer,
        ('POST', ): ArchivalUnitWriteSerializer
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ArchivalUnitFilterClass


class ArchivalUnitDetail(MethodSerializerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchivalUnit.objects.all()
    method_serializer_classes = {
        ('GET', ): ArchivalUnitReadSerializer,
        ('PUT', 'PATCH', 'DELETE'): ArchivalUnitWriteSerializer
    }


class ArchivalUnitSelectList(generics.ListAPIView):
    serializer_class = ArchivalUnitSelectSerializer
    pagination_class = None
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('fonds', 'subfonds', 'series', 'level')
    search_fields = ['title', 'reference_code']
    queryset = ArchivalUnit.objects.all().order_by('fonds', 'subfonds', 'series')
