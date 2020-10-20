from django.urls import path

from . import views

app_name = "Home"

urlpatterns = [
    path('', views.home_view, name = "Home"),
    path('about/', views.about_view, name = 'About')

]
