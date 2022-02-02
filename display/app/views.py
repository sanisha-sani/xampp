from django.shortcuts import render
from app.models import new1
# Create your views here.

def register(request):
    return render(request,'register.html')

def save(request):
    member = new1(name=request.POST['name'], lname=request.POST['lname'], passwd=request.POST['passwd'], email = request.POST['email'],experience=request.POST['experience'])
    member.save()
    return render(request,'home.html')
def show(request):
    vars = new1.objects.all()
    return render(request,'show.html',{'var':vars})