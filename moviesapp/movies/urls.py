# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "movies"

urlpatterns = [
    url(r'^$', view=views.MovieListView.as_view(), name='index'),
    url(r'^(?P<id>[\d\-]+)/$', view=views.MovieDetailView.as_view(), name='detail'),
    url(r'^create/$', view=views.MovieCreateView.as_view(), name='create'),
    url(r'^update/(?P<id>[\d\-]+)/$', view=views.MovieUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<id>[\d\-]+)/$', view=views.MovieDeleteView.as_view(), name='delete'),
    url(r'^rating/(?P<id>[\d\-]+)/$', view=views.MovieRatingView.as_view(), name='rating'),
]
