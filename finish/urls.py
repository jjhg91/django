"""finish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^regalos/', include('apps.gifts.urls')),
    url(r'^partido/', include('apps.plays.urls')),
    url(r'^promociones/', include('apps.promotions.urls')),
    url(r'^social/', include('apps.social.urls')),
    url(r'^', include('apps.sports.urls')),
    url(r'^', include('apps.startContact.urls')),
    url(r'^perfil/', include('apps.users.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
