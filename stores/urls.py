from django.conf.urls import include, url
from django.contrib import admin
from .views import home, store_list, store_detail
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^list$', store_list, name='store_list'),
    url(r'^store/(?P<pk>\d+)/$', store_detail, name='store_detail'),
]
