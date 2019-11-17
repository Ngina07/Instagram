from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'index.html')
