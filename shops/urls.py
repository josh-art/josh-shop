from django.conf.urls import url
from . import views
from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    url(r'^$', views.product_list, name='Home'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^contact me/$', views.contact, name='Contact'),
    url(r'^add user/$', views.addUser, name='AddUser'),
    url(r'^reach me/$', views.feedback, name='reach'),


]
