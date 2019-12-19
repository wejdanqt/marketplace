from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/(?P<id>\d+)$', views.detail),
    url(r'^admin$', views.admin),
    url(r'^add_product$', views.add_product),
    url(r'^p$', views.viewp),
]