from django.conf.urls import include, url
from app.views import *

urlpatterns = [  url(r'^signup/$', 'app.views.start',name='start'), ]
