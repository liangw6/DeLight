from django.shortcuts import render
from django.http import HttpResponse

from .models import IndexCard

def index(request):
  blog_list = IndexCard.objects.order_by('-pub_date')

  return render(request, 'SimpleBlog/index.html', {'blog_list':blog_list})
