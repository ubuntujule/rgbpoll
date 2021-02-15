from django.shortcuts import render
from django.http import HttpResponse
from prettytable import PrettyTable
from django.template import loader

def index(request):
    template = loader.get_template('poll/index.html')
    x = PrettyTable()
    x.field_names= ["member", "boot"]
    context = {'test': 'Test test Test'}
    return HttpResponse(template.render(context, request))
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
