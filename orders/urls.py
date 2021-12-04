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
    path('add/<str:categoria>/<int:uid>',views.add,name="add"),
    # path('remove_from_cart/<int:categoria>/<int:uid>',views.remove_from_cart,name="remove_from_cart"),
]
