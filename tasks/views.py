from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
  
def index(request):
    return render(request, 'tasks/index.html', context={})

def add_collection(request):
    return HttpResponse("")
 