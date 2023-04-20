from django.shortcuts import render, redirect
from .models import Member

# Create your views here.
def register(request):
    if request.method=='POST':
        member=Member(firstname=request.POST['firstname'],lastname=request.POST['lastname'],username=request.POST['username'],password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method=='POST':
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member=Member.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            return render(request, 'login.html')




