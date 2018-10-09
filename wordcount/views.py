from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()

    wordDic = {}

    for word in wordList:
        if word in wordDic:
            #increase
            wordDic[word] += 1
        else:
            #add to dictionary
            wordDic[word] = 1

    sortedwords =  sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'textcount':len(wordList), 'sortedwords':sortedwords}) 

def about(request):
    return render(request, 'about.html')
