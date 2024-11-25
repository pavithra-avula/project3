from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def pavithra(request):
    return HttpResponse('pavithra is a good girl')
def meghana(request):
    return HttpResponse('<h1> My name is meghana</h1>')
def seenu(request):
    return HttpResponse('<h1><marquee> My name is seenu</marquee></h1>')
def manvitha(request):
    return HttpResponse('''
                        <h1> Name is manvitha</h1>
                        <i> Age is 22</i>
                        <b>Gender is Female</b>
                        <img scr="https://tse4.mm.bing.net/th?id=OIP.Mvcr0QDsGXOx29cSBfXd6AHaE7&pid=Api&P=0&h=180" width="300" height="300">                       
                         ''')