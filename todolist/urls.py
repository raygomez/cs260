from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),

    url(r'^add$', views.add),
    url(r'^hello', views.hello),

)
