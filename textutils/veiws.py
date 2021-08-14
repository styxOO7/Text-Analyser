# I have created this file - Tejas
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index2.html')
    # return HttpResponse("<h1>Hello Tejas</h1>") 
 
def analyze(request):
    # get text
    djtext = request.GET.get('text', 'default')
    print(djtext)

    # to check on/off
    removePun = request.GET.get('removePun', 'off')
    capAll = request.GET.get('capAll', 'off')
    removeLines = request.GET.get('removeLines', 'off')
    remExSp = request.GET.get('remExSp', 'off')

    params = {}   # empty dict for variabels in html
    actions = 0   # for number of functions

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    small = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"


    """ Remove punctuations """
    if(removePun == 'on'): 
        actions += 1

        # logical output
        analyzed = ""
        # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed += char

        # variables
        # params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}        

        # variables
        params['analyzed_text'] = analyzed

        # update the djtext for simultaneous functionality
        djtext = analyzed


    """ Capitalize All letters """
    if(capAll == 'on'):

        actions += 1

        # logical Output
        analyzed = djtext.upper()

        # variables
        # params = {'purpose': 'Capitalize All letters', 'analyzed_text': analyzed}        

        # variables
        params['analyzed_text'] = analyzed    

        # update the djtext for simultaneous functionality
        djtext = analyzed  


    """ Remove all end lines """
    if(removeLines == 'on'):
        actions += 1
        analyzed = ""

        # logical output
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed += char
            else: continue

        # variables
        params['analyzed_text'] = analyzed

        # update djtext
        djtext = analyzed
        print(analyzed)


    """ Remove all extra spaces - considers sinlge space valid only. for other cases it takes them empty spaces. """
    if(remExSp == 'on'):
        actions += 1
        analyzed = ""

        # logical output
        i = 0
        while i < len(djtext):
            if djtext[i] == " ":
                point = -1
                for j in range(i, len(djtext)):
                    if djtext[j] != " ":
                        point = j - 1
                        break
                if point != i and point != -1:
                    analyzed += ""
                    i = (point + 1)
                else:
                    analyzed += djtext[i]
                    i += 1 
            else:
                analyzed += djtext[i]
                i += 1 


        # variables
        params['analyzed_text'] = analyzed

        # update djtext
        djtext = analyzed


    # counts
    word_count = 0
    line_count = 0
    pun_count = 0
    small_count = 0
    cap_count = 0
    num_count = 0

    for char in djtext:
        if char == "\n":
            line_count += 1
        if char in punctuations:
            pun_count += 1
        if char in small:
            small_count += 1
        if char in small.upper():
            cap_count += 1
        if char in num:
            num_count += 1
    word_count = len(djtext.split())

    params['wordCount'] = word_count 
    params['numCount'] = num_count
    params['capCount'] = cap_count
    params['smallCount'] = small_count
    params['punCount'] = pun_count
    if len(djtext) != 0: params['lineCount'] = line_count + 1
    else: params['lineCount'] = 0

    params['analyzed_text'] = djtext

    # analyze the text and load the page
    return render(request, 'analyze2.html', params)  # for variables

    
    

# def removePun(request):
#     return HttpResponse("Remove Punctuation")

# def capitalizeFirst(request):
#     return HttpResponse("Capitalize first")

# def spaceRemover(request):
#     return HttpResponse("Remove Spaces")

# def newlineRemover(request):
#     return HttpResponse("Remove new lines")

# def charCount(request):
#     return HttpResponse("Count the characters")