from django.conf.urls import url
from media import views

urlpatterns = [
    url(r'^api/media$', views.media_list, name='get_media_list'),
    url(r'^api/media_details/(?P<pk>[0-9]+)$', views.media_details, name='get_media_details'),
]
