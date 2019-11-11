from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

def homepage(request):
    return render(request = request,
                    template_name="main/home.html",
                    context={"tutorials":Tutorial.objects.all})



def fixtures(request):
    return render(request,"main/fixtures.html")


def view2(request):
    return render(request = request,
                    template_name="main/view2.html",
                    context={"tutorials":Tutorial.objects.all})


