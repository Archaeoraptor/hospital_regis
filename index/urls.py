"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    # 首页的URL
    path('', views.index, name='index'),
    path('/admin/', views.gotoadmin, name='gotoadmin'),
    path('/search.html', views.MySearchView(), name='haystack'),
    path('search2.html', views.MySearchView2(), name='haystacko'),
    path('help.html', views.HelpView, name='help'),

    # path('404.html', views.page_not_found(request=True), name='404'),
    # path('500.html', views.page_error(request=True), name='500'),
    # path(r'^index/', views.index),
    #path('', include('index.urls')),
    #path('user/', include('user.urls'))
]


