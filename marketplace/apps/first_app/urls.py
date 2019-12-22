from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/(?P<id>\d+)$', views.detail),
    url(r'^add_product$', views.add_product),
    url(r'^register$', views.signup),
    url(r'^login$', views.user_login),
    url(r'^logout$', views.user_logout),
  
]