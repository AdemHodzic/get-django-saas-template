from django.urls import path

from . import views

app_name = 'emails'

urlpatterns = [
  path('activate/<str:id>/<str:token>/', views.activate, name='activate'),
  path('activate/success/', views.activate_success, name='activate_success'),
  path('activate/fail/', views.activate_fail, name='activate_fail'),
]