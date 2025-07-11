from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vegies(requests):
    vegies=['spinach','drumsticks','onion','brocoli','brinjal']
    return HttpResponse(f'Available vegies:{vegies}')

def vegies_count(request):
    count=5
    return HttpResponse(f'total number of vegies :{count}')