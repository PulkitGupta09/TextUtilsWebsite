# I have created this file - Pulkit
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    capitalization = request.POST.get('capitalization', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    totalword = djtext
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        totalword = analyzed
    if (newlineremover == 'on'):
        analyzed = ""
        for char in totalword:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        totalword = analyzed
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(totalword):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        totalword = analyzed
    if (capitalization == 'on'):
        analyzed = ""
        for char in totalword:
            analyzed = analyzed + char.upper()
        totalword = analyzed

    if(capitalization == 'on' or extraspaceremover == 'on' or newlineremover == 'on' or removepunc == 'on'):
        params = {'purpose': 'purpose', 'analyzed_text': totalword}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
