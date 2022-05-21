from django.shortcuts import render
from django.http import JsonResponse

def profile(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 266
    }
    return JsonResponse(data)

# Create your views here.
