from django.conf.urls import patterns, url

from participation import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>\d+)/$', views.query, name='query'),                    
)
