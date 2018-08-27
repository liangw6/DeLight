from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from .models import CurrentApp

# Create your views here.
def index(request):
  app_list = CurrentApp.objects.all()
  context = {'app_list':app_list}

  return render(request, 'home/home_page.html', context)
