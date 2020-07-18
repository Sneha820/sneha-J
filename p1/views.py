from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("assignment no 1")
def home(request):
    return HttpResponse("<h1>pyspider basvangudi</h1>")
def html_1(request):
    return render(request,"sample.html")    