from django import views
from django.urls import path 
from codebarapp import views
urlpatterns=[
    path('',views.index, name = 'index'),
    path('ajax', views.ajax, name = 'ajax'),
    path('product/add',views.create_product, name = 'create_product')
]