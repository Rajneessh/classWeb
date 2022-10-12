from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def maths(request):
    return render(request,"webMaths/maths.html")

def add(request):
    return render(request,"webMaths/addition.html")

def sub(request):
    return render(request,"webMaths/sub.html")

def addResult(request):
    val1= 0 if request.GET ['num1']=="" else int(request.GET ['num1'])
    val2= 0 if request.GET ['num2']=="" else int(request.GET ['num2'])
    sum = val1+val2
    return render(request,"webMaths/addResult.html",{'num1':val1, 'num2':val2, 'sum':sum})

def subResult(request):
    val1= 0 if request.GET ['num1']=="" else int(request.GET ['num1'])
    val2= 0 if request.GET ['num2']=="" else int(request.GET ['num2'])
    sub = val1-val2
    return render(request,"webMaths/subResult.html",{'num1':val1, 'num2':val2, 'sub':sub})