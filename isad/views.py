from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from archival_unit.models import ArchivalUnit
from clockwork_api.mixins.method_serializer_mixin import MethodSerializerMixin
from isad.models import Isad
from isad.serializers import IsadSelectSerializer, IsadReadSerializer, IsadWriteSerializer, IsadFondsSerializer, \
    IsadPreCreateSerializer
from django_filters import rest_framework as filters


class IsadFilterClass(filters.FilterSet):
    search = filters.CharFilter(label='Search', method='search_filter')
    status = filters.CharFilter(label='Status', method='filter_status')

    def search_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                (
                    Q(title__icontains=value) |
                    Q(children__title__icontains=value) |
                    Q(children__children__title__icontains=value)
                )
            ).distinct()

    def filter_status(self, queryset, name, value):
        if value == 'not exists':
            return queryset.filter(
                (
                        Q(isad__isnull=True) |
                        Q(children__isad__isnull=True) |
                        Q(children__children__isad__isnull=True)
                )
            ).distinct()
        elif value == 'draft':
            return queryset.filter(
                (
                        Q(isad__published=False) |
                        Q(children__isad__published=False) |
                        Q(children__children__isad__published=False)
                )
            ).distinct()
        else:
            return queryset.filter(
                (
                        Q(isad__published=True) |
                        Q(children__isad__published=True) |
                        Q(children__children__isad__published=True)
                )
            ).distinct()

    class Meta:
        model = ArchivalUnit
        fields = ('fonds',)


class IsadList(generics.ListAPIView):
    queryset = ArchivalUnit.objects.filter(level='F')
    serializer_class = IsadFondsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = IsadFilterClass


class IsadPreCreate(generics.RetrieveAPIView):
    queryset = ArchivalUnit.objects.all()
    serializer_class = IsadPreCreateSerializer


class IsadCreate(generics.CreateAPIView):
    queryset = Isad.objects.all()
    serializer_class = IsadWriteSerializer


class IsadDetail(MethodSerializerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Isad.objects.all()
    method_serializer_classes = {
        ('GET', ): IsadReadSerializer,
        ('PUT', 'PATCH', 'DELETE'): IsadWriteSerializer
    }


class IsadPublish(APIView):
    def put(self, request, *args, **kwargs):
        action = self.kwargs.get('action')
        isad_id = self.kwargs.get('pk')
        isad = get_object_or_404(Isad, pk=isad_id)

        if action == 'publish':
            isad.publish(request.user)
            return Response(status=status.HTTP_200_OK)
        else:
            isad.unpublish()
            return Response(status=status.HTTP_200_OK)


class IsadSelectList(generics.ListAPIView):
    serializer_class = IsadSelectSerializer
    pagination_class = None
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('archival_unit__fonds', 'archival_unit__subfonds', 'archival_unit__series', 'description_level',)
    search_fields = ('reference_code', 'title')
    queryset = Isad.objects.all().order_by('archival_unit__fonds', 'archival_unit__subfonds', 'archival_unit__series')