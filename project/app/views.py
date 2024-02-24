from django.shortcuts import render
from .models import *

# Create your views here.
def app_01(requst):
  return render(requst,"index.html")

def neha(requst):
  if requst.method=="POST":

    name= requst.POST['name']
    email= requst.POST['email']
    course= requst.POST['course']
    fees= requst.POST['fees']
  
    Student.objects.create( name=name,
                                  email=email,
                                  course=course,
                                  fees=fees),
    return render(requst, "index.html", )
  else:

    return render(requst, "index.html", )