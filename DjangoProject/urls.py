"""
URL configuration for DjangoProject project.

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
# from django.contrib import admin
from django.urls import path

import app.views

urlpatterns = [
    path('', app.views.login_view, name='login'),
    path('principal/', app.views.principal_view, name='principal'),
    path('diseno/<int:control_id>/', app.views.diseno_view, name='diseno'),
    path('encabezado/<int:control_id>/', app.views.encabezado_view, name='encabezado'),
    #   path('admin/', admin.site.urls),
]
