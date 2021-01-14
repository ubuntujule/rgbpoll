from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#from random import randit
from prettytable import PrettyTable


def table(self):
    template = loader.get_template('poll/index.html')
    x = PrettyTable()
    x.field_names= ["member", "boot"]
    HttpResponse(template.render(x))
    


#def random_dices():
#    repeat = True
#    while repeat:
#        x = randit(1,6)
#        y = randit(1,6)
#        print(f'You rolled **({x}, {y})**')
#        print(' Roll again? (Y/n)')
#        
#    try 
#    
#    except:
#        raise
#        message = input()
#    repeat = repeat(message)
#def repeat(message = y):
#    
#    
#
#def index(request):
#    dices = random
#    output = 'es klappt'
#    return HttpResponse(output)
## Create your views here.
