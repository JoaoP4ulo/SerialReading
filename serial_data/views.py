from django.shortcuts import render
from django.http import JsonResponse
import serial

def atualizar_variavel(request):
    
    porta_serial = 'COM7' 
    taxa_transmissao = 9600

    arduino = serial.Serial(porta_serial, taxa_transmissao)

    try:
        linha = arduino.readline().decode().strip()
        valor_analogico = int(linha)
        frase_view = f"Valor analógico lido: {valor_analogico}"
    except serial.SerialException:
        frase_view = "Aguardando leitura..."
            
    return render(request, 'dashboard.html', {'frase_view': frase_view})

def dashboard(request):
    return render(request, 'dashboard.html')
