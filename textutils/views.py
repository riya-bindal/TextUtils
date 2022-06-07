# I have created this file - Riya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={'name':'Riya','place':"India"}
    return render(request,'index.html',context)
    return HttpResponse('''<h1>Riya</h1> <a href ="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django CodeWithHarry Playlist</a>''')

def about(request):
    return HttpResponse("About Riya ")

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""   
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Upper Case', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed=""
        for char in djtext:
            if char !='\n' and char!="\r":
                analyzed=analyzed+char.upper()
        params={'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == 'on':
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char.upper()
        params={'purpose':'Removed Spaces', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover != 'on' and newlineremover != 'on' and fullcaps != 'on' and removepunc != 'on':
        return HttpResponse("Please select any operation and try again")
    return render(request, 'analyze.html',params)

def removepunc(request):
    return HttpResponse("Remove Punctuation")

def capfirst(request):
    return HttpResponse("Capitalize first ")

def spaceremove(request):
    return HttpResponse("Space Remover <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("Char Count")

def newlineremove(request):
    return HttpResponse("New Line Remover")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))