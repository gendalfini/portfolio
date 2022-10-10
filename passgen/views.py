from django.shortcuts import render
from django.http import HttpResponse

from random import choice




def passgen(request):
    return render(request, 'passgen.html')

def passgen_output(request):
    symbols=['0123456789','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz','!#$%&*+-=?@^_.']

    result=symbols[2]
    if request.GET.get('uppercase'):
        result+=symbols[1]
    if request.GET.get('special'):
        result+=symbols[3]
    if request.GET.get('numbers'):
        result+=symbols[0]
    amount=int(request.GET.get('amount'))
    lenght=int(request.GET.get('length'))
    passwords=[]

    for j in range(amount):
        thepassword=''
        for i in range(lenght):
            thepassword+=choice(result)
        passwords.append(thepassword)
        thepassword=''


    return render(request, 'passgen_output.html', {'password':passwords})
