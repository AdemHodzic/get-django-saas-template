from django.urls import path

from . import views

app_name = 'emails'

urlpatterns = [
  path('activate/<str:id>/<str:token>/', views.activate, name='activate')
]