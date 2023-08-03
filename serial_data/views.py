from django.shortcuts import render
import random
import requests
import json
import serial 

def atualizar_variavel(request):

    porta_serial = 'COM4'
    taxa_transmissao = 9600

    arduino = serial.Serial(porta_serial, taxa_transmissao)

    try:
        
            # Leia a linha recebida da porta serial do Arduino
        linha = arduino.readline().decode().strip()
            
            # Converta o valor para inteiro (ou float, se necessário)
        valor_analogico = int(linha)
            
            # Faça o que quiser com o valor lido (exemplo: imprimir na tela)

    except serial.SerialException:
        valor_analogico = f"Porta {porta_serial} não reconhecida"
    

    return render(request, 'dashboard.html', {'frase_view': valor_analogico})

