from django.shortcuts import render

def startpage(request):
    return render(request , "community/startpage.html")

# Create your views here.
