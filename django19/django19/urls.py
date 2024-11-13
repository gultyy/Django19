"""
URL configuration for django19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import welcome, sign_up_by_html, platform, games, cart
from task5.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', welcome, name='welcome'),
    path('sign_up/', sign_up_by_html, name='sign_up'),
    path('platform/', platform, name='platform'),
    path('platform/games/', games, name='games'),
    path('platform/cart/', cart, name='cart'),
    path('', post_list, name='posts')
]
