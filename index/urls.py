from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about_as/", views.about_us, name="about_us"),
    path("kontakt/", views.kontakt, name='kontakt'),
    
    
    path('eng/', views.home_eng, name='home_eng'),
    path("about_as/eng/", views.about_us_eng, name="about_us_eng"),
    path('kontakt_eng/', views.kontakt_eng, name='kontakt_eng'),
]