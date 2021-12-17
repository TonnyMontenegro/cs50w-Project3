from django.urls import path
from django.conf import settings
from . import views

from django.conf.urls import handler404
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name="login"),
    path('home', views.menu_view, name="home"),
    path('logout', views.logout_user, name="logout"),
    path('add/<int:uid>/<str:categoria>/',views.add,name="add"),
    path('cart',views.cart,name="cart"),
    path('delete_item/<int:pk>',views.delete_item,name="delete_item"),
    path('make_order/<int:pk>',views.make_order,name="make_order"),
    path('orders',views.orders,name="orders"),
    path('state_change/<str:state>/<int:pk>',views.state_change,name="state_change"),
    path('order/<int:pk>',views.order,name="order")
    # path('remove_from_cart/<int:categoria>/<int:uid>',views.remove_from_cart,name="remove_from_cart"),
]
