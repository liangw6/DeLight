from django.urls import path

from . import views

app_name = 'SimpleBlog'
urlpatterns = [
    path('', views.index, name='index'),
]
