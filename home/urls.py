from django.urls import path
from home import views

app_name = 'home_app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
