"""juniper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from juniper1 import views
from django.contrib.auth.views import logout

urlpatterns = [url(r'^testcoverage/', include('testcoverage.urls')),
#    url(r'^admin/', admin.site.urls),
    url(r'^juniper/', include('juniper1.urls')),
    url(r'^perlscripts/', include('perlscripts.urls')),
    url(r'^defectduplication/', include('defectduplication.urls')), #url(r'^login/$', auth_views.login, name='login'),
#    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^usecase1/', include('usecase1.urls')),
    url(r'^scriptsOptimization/', include('scriptsOptimization.urls')),
    url(r'^AdaptivePlanning/', include('AdaptivePlanning.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

