from django.shortcuts import render
from assignment3.models import User

def InsertUserRecord(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('phonenumber') and request.POST.get('address'):
            saverecord = User()
            saverecord.username = request.POST.get('username')
            saverecord.password = request.POST.get('password')
            saverecord.phonenumber = request.POST.get('phonenumber')
            saverecord.address = request.POST.get('address')

            return render(request, 'index.html')
    else:
        return request(request, 'index.html')