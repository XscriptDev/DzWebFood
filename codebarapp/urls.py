from django import views
from django.urls import path 
from codebarapp import views
urlpatterns=[
    path('', views.index, name = 'index'),
    path('ajax', views.ajax, name = 'ajax'),
    path('product/add', views.create_product, name = 'create_product'),
    path('product/addorupdate', views.retrieve, name = 'retrieve'),
    path('product/list', views.list_product, name = "list_product"),
    path('product/<id>',views.view_product, name='view_product'),
    path('product/<id>/edit',views.update_product, name='edit_product'),
]