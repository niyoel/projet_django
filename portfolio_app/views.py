from django.shortcuts import render

def my_cv(request):
    return render(request,"portofolio_app/portfolio.html")