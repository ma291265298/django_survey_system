from django.http import JsonResponse
from django.shortcuts import render
import json

from survey.models import *


def addView(request):
    return render(request, "login.html")
def erro(request):
    return render(request, "404.html")

def addSuccess(request):
    paper_obj=Paper(name=request.POST.get('paperName'),
                    detail=request.POST.get('paperDetail'))
    paper_obj.save()
    for i in json.loads( request.POST.get('questions')):
        question_obj=Question(no=i['no'],content=i['questionName'],type=i['type'],ismustfill=i['ismustfill'],pid=paper_obj)
        question_obj.save()
        count=1
        for k in i['option']:
            option_obj=Option(no=count,content=k,qid=question_obj)
            count+=1
            option_obj.save()
    return JsonResponse({'resultCode':0})
