from django.shortcuts import render, HttpResponse

# Create your views here.


def post_index(request):
    return HttpResponse('<b>Burası Post index sayfası</b>')


def post_details(request):
    return HttpResponse('<b>Burası Post detail sayfası</b>')


def post_create(request):
    return HttpResponse('<b>Burası Post create sayfası</b>')


def post_update(request):
    return HttpResponse('<b>Burası Post update sayfası</b>')


def post_delete(request):
    return HttpResponse('<b>Burası Post delete sayfası</b>')
