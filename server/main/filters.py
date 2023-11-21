from django.contrib.postgres.search import SearchVector, TrigramSimilarity, TrigramWordSimilarity
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, ExpressionWrapper, F, FloatField, Q
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters

from .models import Project, Technology
from .my_tools import validate_str_to_bool


class CustomSearchFilter(filters.BaseFilterBackend):
    search_param = "search"

    def filter_queryset(self, request, queryset, view):
        search_param = request.GET.get(self.search_param, "").strip()

        if search_param:
            title_similarity = TrigramSimilarity("title", search_param, weight="A")
            description_similarity = TrigramSimilarity("description", search_param, weight="B")
            total_similarity = title_similarity + description_similarity
            queryset = (
                queryset.annotate(
                    description_similarity=description_similarity,
                    title_similarity=title_similarity,
                    total_similarity=total_similarity,
                )
                .filter(total_similarity__gt=0.1)
                .order_by("-total_similarity")
            )

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
        # requested_technologies = request.GET.getlist('technologies')
        requested_technologies = request.GET.get("technologies")
        if requested_technologies:
            technologies_list = requested_technologies.split(",")

            queryset = queryset
            for tech_slug in technologies_list:
                queryset = queryset.filter(technology__slug=tech_slug)
        return queryset


class LinkDeployFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        link_deploy = validate_str_to_bool(request.GET.get("link-deploy"))
        if link_deploy:
            queryset = queryset.filter(link_deploy__isnull=False)
        return queryset


class LinkHubFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        link_hub = validate_str_to_bool(request.GET.get("link-hub"))
        if link_hub:
            queryset = queryset.filter(link_hub__isnull=False)
        return queryset


class StatusFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status_proj = request.GET.get("status")
        if status_proj:
            queryset = queryset.filter(status=status_proj.strip())
        return queryset


class SortFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        sort = request.GET.get("sort")
        if sort:
            sort = sort.strip()
            if "likes" in sort:
                queryset = queryset.annotate(likes_count=Count("likes")).order_by(sort + "_count")
            if "created" in sort:
                queryset = queryset.order_by(sort)
        return queryset
