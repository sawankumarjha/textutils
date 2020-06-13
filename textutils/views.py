from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')
def analyze(request):
    value =request.POST.get('Menu','off')
    djtext=request.POST.get('text','default')

    analyzed=""


    if value == '0':
        punctuation = string.punctuation

        for char in djtext:
            if char not in punctuation:
                analyzed += char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif (value == '1'):
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed += char
            params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (value == '2'):
        analyzed = djtext.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (value == '3'):
        l = len(djtext)
        params = {'purpose': 'Character Counter', 'analyzed_text': l}
        return render(request, 'analyze.html', params)

    elif (value == '4'):
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed += char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (value == '5'):

        analyzed = djtext.lower()
        params = {'purpose': 'Lower Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Something wrong")




def about(request):
    return render(request,"about.html")
