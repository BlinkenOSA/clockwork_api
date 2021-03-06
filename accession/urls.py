from django.urls import path

from accession.views.accession_views import AccessionList, AccessionDetail, AccessionSelectList, AccessionPreCreate
from accession.views.select_views import AccessionMethodSelectList, AccessionCopyrightStatusSelectList


app_name = 'accession'

urlpatterns = [
    path('', AccessionList.as_view(), name='accession-list'),
    path('<int:pk>/', AccessionDetail.as_view(), name='accession-detail'),
    path('create/', AccessionPreCreate.as_view(), name='accession-pre-create'),
    path('select/', AccessionSelectList.as_view(), name='accession-select-list'),

    # Select URLs
    path('select/accession_copyright_status/', AccessionCopyrightStatusSelectList.as_view(),
         name='accession_copyright_status-select-list'),
    path('select/accession_method/', AccessionMethodSelectList.as_view(),
         name='accession_method-select-list'),
]