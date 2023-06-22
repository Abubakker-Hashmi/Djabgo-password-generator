from django.shortcuts import render
from django.http import HttpResponse                                   #should be imported 
import random       
def home(request):
    return render(request,'home.html')                                         #you can pass dictionary here. 
def password(request):
   
    ranpas=''
    vl=list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',4))
 
    if request.GET.get('Uppercase'):
        vl.extend(list('ABCDEGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        vl.extend(list('1234567890'))    
    if request.GET.get('specialcase'):
        vl.extend(list('!@#$%^&*()'))   
    v=list(vl)
    

    for x in range(length): 
        ranpas=ranpas+random.choice(vl)
    return render (request,'password.html',{'password':ranpas})
# Create your views here.
