from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<slug>[A-z0-9_-]+)/$', views.detail, name='detail'),
]