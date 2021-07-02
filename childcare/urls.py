from django.urls import path

from . import views

app_name = "childcare"

urlpatterns = [
    path("", views.ChildcareHome.as_view(), name="home"),
    path("search/", views.ChildcareSearch.as_view(), name="search"),
    path("stats/", views.ChildcareStats.as_view(), name="stats"),
]
