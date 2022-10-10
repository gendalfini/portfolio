from django.shortcuts import render
from django.http import HttpResponse

from random import choice




def caesar(request):
    return render(request, 'caesar.html')

def caesar_output(request):
    rus=[i for i in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
    rus_low=[i.lower() for i in rus]
    eng=[chr(i) for i in range(65,91)]
    eng_low=[i.lower() for i in eng]

    step=int(request.GET.get('step'))
    txt=str(request.GET.get('text'))
    goal = int(request.GET.get('shifr'))





    def shifr(txt,step):
        out_text=''

        for i in range(len(txt)):

            if txt[i].upper() not in rus and txt[i].upper() not in eng:
                out_text+=txt[i]
                continue

            if txt[i].upper() in rus:
                step=(int(step)%32)
                if txt[i].upper()==txt[i]:
                    out_text+=rus[(step+rus.index(txt[i]))%32]
                    continue
                else:
                    out_text+=rus_low[(step+rus_low.index(txt[i]))%32]
                    continue
            if txt[i].upper() in eng:
                step=(int(step)%26)
                if txt[i].upper()==txt[i]:
                    out_text+=eng[(step+eng.index(txt[i]))%26]
                    continue
                else:
                    out_text+=eng_low[(step+eng_low.index(txt[i]))%26]
                    continue
        return out_text



    def deshifr(text,step):

        out_text=''
        for i in range(len(text)):

            if txt[i].upper() not in rus and txt[i].upper() not in eng:
                out_text+=txt[i]
                continue

            if txt[i].upper() in rus:
                step=(int(step)%32)
                if txt[i].upper()==txt[i]:
                    out_text+=rus[(-step+rus.index(txt[i]))%32]
                    continue
                else:
                    out_text+=rus_low[(-step+rus_low.index(txt[i]))%32]
                    continue
            if txt[i].upper() in eng:
                step=(int(step)%26)
                if txt[i].upper()==txt[i]:
                    out_text+=eng[(-step+eng.index(txt[i]))%26]
                    continue
                else:
                    out_text+=eng_low[(-step+eng_low.index(txt[i]))%26]
                    continue

        return out_text

    out=''

    if goal==0:
        out_text=shifr(txt,step)

    if goal==1:
        out_text=deshifr(txt,step)




    return render(request, 'caesar_output.html', {'out_text':out_text})
