from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_username', views.add_username),
    url(r'^success', views.success),
]
