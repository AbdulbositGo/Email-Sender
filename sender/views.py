from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy


def index(request):
    sleepy.delay()
    return HttpResponse("Hello world with sleepy")