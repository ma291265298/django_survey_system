from django.http import HttpResponse
from django.shortcuts import render
def addView(request):
    return render(request, "add.html")
def erro(request):
    return render(request, "404.html")
def addSuccess(request):
    try:
        if request.POST['username']=='sb110':
            return render(request, "success.html")
        return render(request, "404.html")
    except:
        return render(request, "404.html")
