from django.shortcuts import render
from . import models
def home(request):
    homepage= models.Home.objects.all()
    return render(request, 'page.html', {"homepage": homepage})
