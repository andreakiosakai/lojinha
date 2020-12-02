from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('registro/', views.register, name='register'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password')
]

