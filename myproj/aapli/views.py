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
