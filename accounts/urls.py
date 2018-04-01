from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
