# 1) Crie uma função chamada "mostrar_hora" que imprime a hora atual do sistema
from datetime import datetime

def mostrarHora():
    hora = datetime.now().strftime("%H")
    minutos = datetime.now().strftime("%M")
    segundos = datetime.now().strftime("%S")
    print(f"{hora}:{minutos}:{segundos}")

print("--------- HORA ATUAL ---------")
mostrarHora()