"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     #path("activity/", include("activity.urls")),
#     path("client/", include("client.urls")),
#     #path("inventory/", include("inventory.urls")),
#     #path("sale/", include("sale.urls")),
#     path("", include("general.urls")),
#     path("admin/", admin.site.urls),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inventory/", include("inventory.urls")),
    path("client/", include("client.urls")),
    path("home/", include("general.urls"), name="home"),
    path("",lambda _: redirect("general:home")),
    path("sale/", include("sale.urls")),
    # path("activity/", include("activity.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
