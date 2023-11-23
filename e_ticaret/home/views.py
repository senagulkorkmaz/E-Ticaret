from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = "Merhaba Senagül"
    context = {"text": text}
    return render(request, "index.html", context)
