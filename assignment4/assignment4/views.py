from django.shortcuts import render
from django.http import HttpResponse
from .models import User
def home(request):
    return render(request, 'index.html')

def addrecord(request):
    if request.method =='POST':
        if request.POST.get('username') and request.POST.get('passwd') and request.POST.get('phonenumber') and request.POST.get('address'):
            user = User()
            user.username = request.POST.get('username')
            user.phonenumber = request.POST.get('phonenumber')
            user.passwd = request.POST.get('passwd')
            user.address = request.POST.get('address')
            user.save()
            return render(request, 'viewrecord.html', )
    else:
        return render(request, 'addrecord.html')

def viewrecord(request):
    users = User.objects.all()
    print(users)
    return render(request, 'viewrecord.html', {'user': users})