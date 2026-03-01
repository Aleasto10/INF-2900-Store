from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('htmlfile/', views.render_html, name='render_html'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    #Cart
    path("api/cart/<int:account_id>/", views.get_cart),
    path("api/cart/add/", views.add_to_cart),
    path("api/cart/decrease/", views.decrease_from_cart),
    path("api/cart/remove/", views.remove_from_cart),
    path("api/cart/checkout/", views.checkout),
    path('api/products/', views.product_list, name='product_list'),
]