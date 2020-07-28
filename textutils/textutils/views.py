###my webiste
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # c='''
    # # <h2>MY WEBSITE</h2>
    # # <p><a href="https://www.w3.org/">W3C</a></p>
    # #      <p><a href="https://www.google.com/">Google</a></p>
    # #      <p><a href="http://127.0.0.1:8000/about/">About</a></p>
    # #
    # #      '''
    # # return HttpResponse(c)

    return render(request, 'index.html')



def about(request):
    return render(request,'about.html')


def analyze(request):
    djtext = (request.GET.get('text', 'default'))
    removepunc = (request.GET.get('removepunc', 'off'))
    fullcaps = (request.GET.get('fullcaps', 'off'))
    newlineremover = (request.GET.get('newlineremover', 'off'))
    extraspaceremover = (request.GET.get('extraspaceremover', 'off'))
    print(djtext)
    print(removepunc)
    print(fullcaps)
    print(newlineremover)
    print(extraspaceremover)

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    analyzed = djtext
    params={}
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                no_punct = no_punct + char

        analyzed = no_punct
        params = {'purpose': "remove punctuations", 'analyzed_text': analyzed}
    if fullcaps == 'on':
        analyzed = analyzed.upper()
        params = {'purpose': "fullcaps", 'analyzed_text': analyzed}
    if newlineremover == 'on':
        analyzed = analyzed.strip()
        params = {'purpose': "newlinw removal", 'analyzed_text': analyzed}
    if extraspaceremover == 'on':
        analyzed = analyzed.replace(" ", "")
        params = {'purpose': "extra psace remover", 'analyzed_text': analyzed}
    else:
        analyzed = djtext


    return render(request, 'analyze.html', params)


def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))
