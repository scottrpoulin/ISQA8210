from . import views
from django.urls import path

app_name = 'snek'
urlpatterns = [
    path('home/', views.home, name='home'),
]