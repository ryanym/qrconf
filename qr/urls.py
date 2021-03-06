from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<file_id>[0-9]+)/$', views.display, name='display'),
    url(r'^(?P<file_id>[0-9]+)/confirm$', views.confirm, name='confirm'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
