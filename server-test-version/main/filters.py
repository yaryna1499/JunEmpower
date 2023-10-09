from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity, TrigramWordSimilarity
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import filters
from django.db.models import Q, Count, F, FloatField, ExpressionWrapper
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Technology
from .my_tools import validate_str_to_bool


class CustomSearchFilter(filters.BaseFilterBackend):
    search_param = 'search'

    def filter_queryset(self, request, queryset, view):
        search_param = request.GET.get(self.search_param, '').strip()

        if search_param:
            title_similarity = TrigramSimilarity('title', search_param, weight='A')
            description_similarity = TrigramSimilarity('description', search_param, weight='B')
            total_similarity = title_similarity + description_similarity
            queryset = queryset.annotate(description_similarity=description_similarity,
                                         title_similarity=title_similarity,
                                         total_similarity=total_similarity
                                         ).filter(total_similarity__gt=0.1).order_by('-total_similarity')

            # queryset = queryset.annotate(title_similarity=TrigramSimilarity('title', search_param),
            #                              description_similarity=TrigramSimilarity('description', search_param)
            #                              ).filter(
            #                                     title_similarity__gt=0.1,  # Минимальное сходство для заголовка
            #                                     description_similarity__gt=0.1,  # Минимальное сходство для описания
            #                                 ).annotate(
            #                                     weighted_similarity=F('title_similarity') * 0.7 + F('description_similarity') * 0.3
            #                                 ).order_by('-weighted_similarity')

            # title_weight = 0.7
            # description_weight = 0.3

            # title_similarity = TrigramWordSimilarity('title', search_param)
            # description_similarity = TrigramWordSimilarity('description', search_param)
            # total_similarity = ExpressionWrapper(
            #     title_similarity + description_similarity,
            #     output_field=FloatField()
            # )
            #
            # queryset = queryset.annotate(description_similarity=description_similarity,
            #                              title_similarity=title_similarity,
            #                              total_similarity=total_similarity
            #                              ).filter(total_similarity__gt=0.1).order_by('-total_similarity')

        return queryset


class TechnologiesFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        requested_technologies = request.GET.getlist('technologies')
        queries = []
        for tech in requested_technologies:
            try:
                Technology.objects.get(slug=tech)
                queries.append(Q(technology__slug=tech))
            except ObjectDoesNotExist:
                # Якщо треба буде тут можно обробити випадок коли така технолгія відсутня в БД, або вказана з помилкою
                pass

        result_query = Q()
        for query in queries:
            result_query &= query
        queryset = queryset.filter(result_query)
        return queryset


class LinkDeployFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        link_deploy = validate_str_to_bool(request.GET.get('link-deploy'))
        if link_deploy:
            queryset = queryset.filter(link_deploy__isnull=False)
        return queryset


class LinkHubFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        link_hub = validate_str_to_bool(request.GET.get('link-hub'))
        if link_hub:
            queryset = queryset.filter(link_hub__isnull=False)
        return queryset


class StatusFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status_proj = request.GET.get('status')
        if status_proj:
            queryset = queryset.filter(status=status_proj.strip())
        return queryset


class SortFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        sort = request.GET.get('sort')
        if sort:
            sort = sort.strip()
            if 'likes' in sort:
                queryset = queryset.annotate(likes_count=Count('likes')).order_by(sort + '_count')
            if 'created' in sort:
                queryset = queryset.order_by(sort)
        return queryset
