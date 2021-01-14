from django.shortcuts import render
from django.http import HttpResponse
from prettytable import PrettyTable


def index(request):
#    template = loader.get_template('poll/index.html')
    x = PrettyTable()
    x.field_names= ["member", "boot"]
    return HttpResponse(x)
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
