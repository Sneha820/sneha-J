from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("assignment no 1")

def home(request):
    return Http("<h1>pyspriders basvangudi</h1>")   

def html_1(request):
    return render(request,"sample.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"sneha",'name':"neha"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':20})
