from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.user_list),
    path('add/', views.user_add),
]
