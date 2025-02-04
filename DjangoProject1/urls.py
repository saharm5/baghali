"""
URL configuration for DjangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home\
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .data import get_data
from django.contrib import admin
from .categories import get_data_categories
from django.urls import path
from DjangoProject1.views import plist, recievemsg

urlpatterns = [
    path('data/', get_data, name='get_data'),
    path('admin/', admin.site.urls),
    path('plist/', plist),  # URL pattern for the plist view
    path('regmsg/', recievemsg),  # URL pattern for receiving messages via POST
    path('categories/', get_data_categories, name='get_data_categories'),
    path('save-data/', recievemsg),  # Same as above (POST for saving data)

]
