"""cota URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Core Urls
    path('', include('core.urls')),
    # Nodos Urls
    path('nodos/', include('nodos.urls')),
    # About Urls
    path('about/', include('about.urls')),
    # Contact
    path('contact/', include('contact.urls')),
    # Admin
    path('admin/', admin.site.urls),
    # Pages
    path('page/', include('pages.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom title for admin
admin.site.site_header = 'Proyecto "COTA"'
admin.site.index_title = 'Panel de Administrador'
admin.site.site_title = 'COTA'