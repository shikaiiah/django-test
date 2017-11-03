from django.conf.urls import url

from myapp01 import views

urlpatterns = [
    url(r'^$', views.index),
]
