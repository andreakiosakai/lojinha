from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<slug>\w+)/$', views.category, name='category'),
]