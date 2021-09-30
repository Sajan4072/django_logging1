from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def addUser(request):
    val={
        'response':'User Added'

    }
    print("hello addUser")
    status=200
    return JsonResponse(val,status=status)


def addSomething(request):
    val={'response':'something added'}
    return JsonResponse(val,status=200)

def addNew(request,someNumber):
    val={'response':'something Added New','numberGiven':int(someNumber)}
    if int(someNumber) > 50:
        return JsonResponse(val,status=500)
    else:
        return JsonResponse(val,status=200)    
