"""ajaxdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from blog.views import start, create_post, get, getmoreinfo, put1, put2, put3, delete, deleteTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start, name="start"),
    path('post', create_post, name="create"),
    path('get', get, name="get"),
    path('get/moreinfo/<int:id>', getmoreinfo, name="getmoreinfo"),
    path('deleteItem/<int:pk>', delete, name="delete"),
    path('delete/', deleteTest, name="delete"),
    path('put1/', put1, name="put1"),
    path('put2/<int:pk>', put2, name="put2"),
    path('put3/<int:pk>', put3, name="put3")
]
