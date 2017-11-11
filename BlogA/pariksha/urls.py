"""pariksha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from papp.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login),
    url(r'^updates/$',info_f),
    url(r'^signup/$',signup,name='signup'),
    url(r'^auth-check/$',auth_view,name='check'),
    url(r'^blogs/$',blogs,name='blogs'),
    url(r'^logout/$',logout),
    url(r'^search_query/$',search),
    url(r'^delete/(\d+)/$',delete, name='delete'),
    url(r'^Comment/$',Comment, name='Comment'),
    url(r'^dashboard/(\d+)/$',dashboard,name='dashboard'),
    url(r'^profile/$',user_profile,name='profile'),
] + static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)
