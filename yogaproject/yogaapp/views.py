from django.http import HttpResponse
from django.shortcuts import render
from.models import place
# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,"hello.html",{'obj':name})
# def about (request):
#     return render(request, "about.html")
# def addition (request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y

def demo(request):
    obj=place.objects.all()


    return render(request,"index.html",{'result':obj})