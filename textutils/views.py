from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') #when we go to the url/index this method gets called and then index.html is used

def analyse(request):
    djtext = request.GET.get('text', 'default') #gets value of textbox named 'text' otherwise it will take 'default'
    removepunc = request.GET.get('removepunc', 'off') 
    fullcaps = request.GET.get('fullcaps', 'off')
    print(removepunc)
    print(fullcaps)
    print(djtext)
    # analysed = djtext
    punctuations = '''!()-[]{};:':\,<>./?@#$%^&*_~'''
    analysed = ""
    if removepunc == "on":
     for char in djtext:
        if char not in punctuations:
            analysed = analysed + char
            params = {'purpose':'Removed Punctuations', 'analysed_text':analysed}
      
    elif fullcaps == "on":
     djtext = djtext.upper()
     analysed = djtext
     params = {'purpose':'Changed to uppercase', 'analysed_text':analysed}

    return render(request, 'analyse.html', params)

# def capfirst(request):
#     return HttpResponse("capfirst")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("charcount")