from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text 
    djtext = request.POST.get('text','default')

    # check button is on or off 
    removePunc = request.POST.get('removePunc','off')
    fullCaps = request.POST.get('fullCaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    # if removePunc button is on then it code will be run 
    Punctuation = '''[]{}-!"#$%&'()*+,./:;<=>?@\^_`\|'''
    if removePunc == 'on':
        analyze_text = ""
        for char in djtext:
            if char not in Punctuation:
                analyze_text = analyze_text + char

        params = {'purpose' : 'Removed Punctuation', 'analyze_text' : analyze_text}
        djtext = analyze_text
        # return render(request, 'analyze.html', params)

    # if fullCaps button is on then it code will be run
    if fullCaps == 'on':
        analyze_text = ""
        for char in djtext:
            analyze_text = analyze_text + char.upper()

        params = {'purpose' : 'Change to upper case', 'analyze_text' : analyze_text}
        djtext = analyze_text
        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyze_text = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze_text = analyze_text + char

        params = {'purpose' : 'Remove new line', 'analyze_text' : analyze_text}
        djtext = analyze_text
        # return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyze_text = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyze_text = analyze_text + char
            
        params = {'purpose' : 'Remove extra space', 'analyze_text' : analyze_text}
        djtext = analyze_text
        # return render(request, 'analyze.html', params)

    if charcount == 'on':
        count = str(len(djtext))
        analyze_text = (f"Number of character, you have enter " + count)
            

        params = {'purpose' : 'Counte the characters', 'analyze_text' : analyze_text}
        djtext = analyze_text
        # return render(request, 'analyze.html', params)

    if (removePunc != 'on' and fullCaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse("Please choose at least one option")
    return render(request, 'analyze.html', params)