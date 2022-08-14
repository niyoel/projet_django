from django.shortcuts import render

def my_cv(request):
    return render(request, "cv_app/home.html")