"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from inventory.api import BooklistAPI,BookDetailAPI,CategorylistAPI,CategoryDetailAPI,AuthorlistAPI,AuthorDetailAPI,BookCreateAPI,BooKUpdateAPI,BooKDeleteAPI

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('auth/', include('rest_authtoken.urls')),


    #===============API URLS=================
    path('inventory/api',BooklistAPI.as_view()),
    path('inventory/api/<int:pk>',BookDetailAPI.as_view()),
    path('inventory/api/create',BookCreateAPI.as_view()),
    path('inventory/api/update/<int:pk>',BooKUpdateAPI.as_view()),
    path('inventory/api/delete/<int:pk>',BooKDeleteAPI.as_view()),

    path('inventory/category/api',CategorylistAPI.as_view()),
    path('inventory/category/api/<int:pk>',CategoryDetailAPI.as_view()),


    path('inventory/author/api',AuthorlistAPI.as_view()),
    path('inventory/author/api/<int:pk>',AuthorDetailAPI.as_view()),


    #==================SWAGGER===============================
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 
]


urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

