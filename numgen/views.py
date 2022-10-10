from django.shortcuts import render
from django.http import HttpResponse
from random import choice


def numgen(request):
    return render(request, 'numgen.html')

def numgen_output(request):
    import random
    number=[]
    amount=int(request.GET.get('amount'))
    diapazon1=int(request.GET.get('diapazon1'))
    diapazon2=int(request.GET.get('diapazon2'))
    if request.GET.get('integer'):
        for i in range(amount):
            number.append(random.randint(diapazon1,diapazon2))
    else:
        for i in range(amount):
            number.append(random.uniform(diapazon1,diapazon2))
    return render(request, 'numgen_output.html', {'numbers':number})
