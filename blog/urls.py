from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views


urlpatterns = [ 
                url(r'^$', views.post_list, name="post_list"),

                url(r'^(?P<pk>\d+)$', views.post_detail, name='post_detail'),
      
            ]