from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
       url(r'^$',views.home,name='Home'),
       url(r'^new_neighbourhood',views.new_neighbourhood,name='new_neighbourhood'),
       url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,
]
