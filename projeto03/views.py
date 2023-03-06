from django.shortcuts import render, HttpResponse


def Home(requests):
    return HttpResponse("OK!")

