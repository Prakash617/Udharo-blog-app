"""blogapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
# router.register(r'login', ProductViewSet, basename='Product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("api.urls")),
    path('udharo/',include("udharo.urls")),
    path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('auth.urls')),
    path('', include(router.urls)),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
