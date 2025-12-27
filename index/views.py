from django.shortcuts import render
from django.http import HttpResponse
from .models import Punt_tonal, Punet_qe_bejm

# Create your views here.


def home(request):
    punet_tonal = Punt_tonal.objects.all()
    punet_qe_bejm = Punet_qe_bejm.objects.all()
    return render(request, "index/home.html", {'punet_tonal': punet_tonal, 'punet_qe_bejm': punet_qe_bejm})


def home_eng(request):
    punet_tonal = Punt_tonal.objects.all()
    punet_qe_bejm = Punet_qe_bejm.objects.all()
    return render(request, "index/home_eng.html", {"punet_tonal": punet_tonal, "punet_qe_bejm": punet_qe_bejm})


def kontakt(request):
    return render(request, "index/kontakt.html", {})


def kontakt_eng(request):
    return render(request, "index/kontakt_eng.html", {})


def about_us (request):
    return render(request, "index/about_us.html", {})


def about_us_eng (request):
    return render(request, "index/about_us_eng.html", {})