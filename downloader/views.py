from django.shortcuts import render
from django.http import HttpResponse

import pafy



def downloader(request):
    return render(request, 'downloader.html')

def downloader_out(request):
    url=str(request.GET.get('adr'))
    goal = str(request.GET.get('option'))

    v=pafy.new(url)
    streams=v.streams
    if goal=='VA':
        streams=v.streams

    elif goal=='V':
        streams=v.videostreams

    elif goal=='A':
        streams=v.audiostreams


    title=v.title
    qualitys=[]
    durls=[]

    for i in streams:
        qualitys.append(i.quality)
        durls.append(i.url)

    return render(request, 'downloader_out.html',context={'title':title,'qualitys':qualitys,'durls':durls})
