from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'pro.views.home', name='home'),
    url(r'^app/', include('app.urls')),
    #url(r'^app/test$','app.views.start'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/signup/thankyou/$',TemplateView.as_view(template_name='thankyou.html')),
]
