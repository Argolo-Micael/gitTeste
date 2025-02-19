from datetime import datetime

Nome = input("Insira seu Nome: ")
idade = int(input('digite sua idade: '))
Agora = datetime.now()
Data = Agora.strftime("%d/%m/%Y")
Hora = Agora.strftime("%H:%M")

print(f'seu nome é {Nome}, sua idade é {idade}')
print(f"Data: {Data} Hora: {Hora}")
if Hora <= '12:00':
    print(f'bom dia {Nome}')
elif Hora <= '18:00':
    print(f'boa tarde {Nome}')
else:
    print(f'boa noite {Nome}')


