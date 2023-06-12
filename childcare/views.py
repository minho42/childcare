from difflib import get_close_matches

from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Childcare
from .serializers import ChildcareSerializer


class ChildcareHome(APIView):
    permission_classes = []
    http_method_names = ["get"]

    def get(self, request):
        return Response({"data": "It's working!"})


class ChildcareStats(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get"]

    def get(self, request):
        try:
            last_update = Childcare.objects.order_by("-modified")[1].modified
        except IndexError:
            last_update = ""
        total_count = Childcare.objects.count()
        data = {"lastUpdate": last_update, "totalCount": total_count}
        return Response(data)


class ChildcareSearch(generics.ListAPIView):
    serializer_class = ChildcareSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        query = self.request.query_params.get("q", None)
        if not query:
            return None

        result = Childcare.objects.filter(
            Q(name__icontains=query)
            | Q(address__icontains=query)
            | Q(suburb__icontains=query)
            | Q(postcode__exact=query)
        ).order_by(
            "-overall_rating_number",
            "-average_ratings",
            "-prev_overall_rating_number",
            "-prev_average_ratings",
            "name",
        )[
            :100
        ]
        if result.count() > 0:
            return result

        unique_suburbs = list(
            Childcare.objects.order_by().values_list("suburb").distinct()
        )  # list of tuples [('RYDE',), ]
        unique_suburbs = [u[0] for u in unique_suburbs]

        possible_matches = get_close_matches(query.upper(), unique_suburbs, cutoff=0.8)
        if not possible_matches:
            return None
        result = Childcare.objects.filter(suburb__icontains=possible_matches[0]).order_by(
            "-overall_rating_number",
            "-average_ratings",
            "-prev_overall_rating_number",
            "-prev_average_ratings",
            "name",
        )[:100]
        return result
