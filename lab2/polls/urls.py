from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('get', views.get, name='get'),
    path('', views.create_post, name='create'),
]