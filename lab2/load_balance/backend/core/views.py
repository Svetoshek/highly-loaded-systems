from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
import os

def index(request):
    return JsonResponse({"message": "Welcome"})

def status(request):
    port = os.getenv("PORT", 5001)
    return JsonResponse({"service": "backend", "port": port})

def data(request):
    return JsonResponse({"value": random.randint(1, 100)})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
