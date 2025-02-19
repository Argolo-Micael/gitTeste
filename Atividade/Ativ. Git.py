from datetime import datetime

Nome = input("Insira seu Nome: ")
idade = int(input('digite sua idade: '))
Agora = datetime.now()
Data = Agora.strftime("%d/%m/%Y")
Hora = Agora.strftime("%H:%M")


print(f"Data: {Data} Hora: {Hora}")