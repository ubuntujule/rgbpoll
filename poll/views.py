import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    create_entries()
    template = loader.get_template('poll/index.html')
    #x = PrettyTable()
    #x.field_names= ["member", "boot"]
    context = {}
    context['header'] = 'RGB PLaner'
    context['theader'] = ['WER?', 'Datum', 'Von', 'Bis', 'Notizen']
    #member, date, ontime, offtime, notes
    if request.GET:

        print(request.GET.get("member")) 
        entries['member'] = request.GET.get("member")
        entries['date'] = request.GET.get("date")
        entries['ontime'] = request.GET.get("ontime")
        entries['offtime'] = request.GET.get("offtime")
        entries['notes'] = request.GET.get("notes")

        save_on_json() 
    return HttpResponse(template.render(context, request))
    
def save_on_json():
    with open("rgb.json", "w") as _file:
        json.dump(entries, _file)
    return 

    
def create_entries():
    global entries
    try:
        with open("rgb.json") as f:
            entries = json.load(f)
            print(entries)
    except FileNotFoundError:
        entries = {} 
