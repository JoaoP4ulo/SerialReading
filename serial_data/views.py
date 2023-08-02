from django.shortcuts import render
import random
import requests
import json

def atualizar_variavel(request):
    frase_view = random.randint(1, 100)
    print(frase_view)
    return render(request, 'dashboard.html', {'frase_view': frase_view})

