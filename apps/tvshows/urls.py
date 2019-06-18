from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/(?P<showid>\d+)$', views.display_show),
    url(r'^shows/new$', views.new_show),
    url(r'^addShowToDB$', views.addShowToDB),
    url(r'^editShowtoDB/(?P<showid>\d+)$', views.editShowtoDB),
    url(r'^shows/(?P<showid>\d+)/delete$', views.delete_show),
    url(r'^shows/(?P<showid>\d+)/edit$', views.edit_show),

]
