from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r'adicionar/(?P<slug>[\w_-]+)/$',
        views.create_cartitem,
        name='create_cartitem'
    ),
    path('', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    path('meus-pedidos/', views.order_list, name='order_list')
]