from django.urls import path

from . import views

app_name = 'arapp'
urlpatterns = [
  path('', views.top, name='top'),
]