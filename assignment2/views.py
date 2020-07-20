from django.shortcuts import render
import math
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def bmi(request):
    if request.method == "GET":
        height = float(request.GET['height'])
        weight = float(request.GET['weight'])
        print(height, weight)
        bmi = (float(weight)/float(height*height))
        if(bmi < 18.5):
            BMI = str(bmi)
            return HttpResponse("BMI is "+BMI+" and you are UnderWeight")
        if(18.5 < bmi < 24.9):
            BMI = str(bmi)
            return HttpResponse("BMI is "+BMI+" and you are Normal Weight")
        if(25 < bmi < 29.9):
            BMI = str(bmi)
            return HttpResponse("BMI is "+BMI+" and you are Over Weight")
        if(bmi >= 30):
            BMI = str(bmi)
            return HttpResponse("BMI is "+BMI+" and you have obesity")
    
