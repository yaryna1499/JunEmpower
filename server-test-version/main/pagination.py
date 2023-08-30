from rest_framework.pagination import PageNumberPagination

from django.conf import settings


class CustomSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
