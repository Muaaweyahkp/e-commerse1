from django.contrib import admin
from django.urls import path
from .import views
app_name="web"

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('blog',views.blog ,name = 'blog'),
    path('contact',views.contact,name = 'contact'),
    path('category',views.category,name = 'category'),
    path('cart',views.cart,name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('confirmation', views.confirmation, name = 'confirmation'),
    path('singleProduct',views.singleProduct, name = 'singleProduct'),
    path('tracking', views.tracking, name = 'tracking'),
    path('login', views.login, name = 'login'),
    path('elements', views.elements, name = 'elements'),
    path('singleBlog', views.singleBlog, name = 'singleBlog') 
]
