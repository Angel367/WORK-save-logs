from django.urls import path

from . import views

urlpatterns = [
    path('add_log/', views.create_search_log, name='search'),
]