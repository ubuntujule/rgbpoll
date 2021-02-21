from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('poll/index.html')
    #x = PrettyTable()
    #x.field_names= ["member", "boot"]
    context = {}
    context['header'] = 'RGB PLaner'
    context['theader'] = ['WER?', 'Datum', 'Von', 'Bis', 'Notizen']
    print(request.GET.get("date")) 
    return HttpResponse(template.render(context, request))
    
