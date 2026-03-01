from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('htmlfile/', views.render_html, name='render_html'),
    path('api/products/', views.product_list, name='product_list'),
]