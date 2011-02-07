from django.conf.urls.defaults import *
from openid_consumer.views import complete, signout
from django.views.generic.simple import direct_to_template

#Login Views
urlpatterns = patterns('',
  url(r'^connect/$', 'sso.views.connect'),
  url(r'^login/$', 'sso.views.login_server'),
  url(r'^register/$', 'sso.views.register'),
  url(r'^generate/$', 'sso.generate.key'),
  url(r'^logout/$', 'sso.views.logout'),
  url(r'^check/(?P<user_id>\d+)/(?P<token>\w+)/$', 'sso.views.check'),
  url(r'^send/(?P<client>\w+)/$', 'sso.views.send'),
)