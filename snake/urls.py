from django.conf.urls import patterns, include, url

from snake import views


urlpatterns = patterns(
    '',
    url(r'^scores/', views.scores),
)
