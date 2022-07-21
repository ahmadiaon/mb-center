from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.employee, name='employee'),
    path('profile/<str:pk>', views.profile, name='profile')
]