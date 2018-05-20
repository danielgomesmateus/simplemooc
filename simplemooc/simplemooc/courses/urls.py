from django.urls import path, re_path
from . import views  

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name = 'index'),
    #re_path(r'^details/(?P<id>\d+)/$', views.details, name = 'details')
    re_path(r'^details/(?P<slug>[\w_-]+)/$', views.details, name = 'details')
]