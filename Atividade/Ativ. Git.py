from datetime import datetime
from random import randint
Nome = input("Insira seu Nome: ")
idade = int(input('digite sua idade: '))
Agora = datetime.now()
Data = Agora.strftime("%d/%m/%Y")
Hora = Agora.strftime("%H:%M")


if Hora <= '12:00':
    print("")
    print(f'Bom dia! {Nome} de {idade} anos, a Data e a Hora atual são {Data} {Hora}')
    print("")
elif Hora <= '18:00':
    print("")
    print(f'Boa tarde! {Nome} de {idade} anos, a Data e a Hora atual são {Data} {Hora}')
    print("")
else:
    print("")
    print(f'Boa noite! {Nome} de {idade} anos, a Data e a Hora atual são {Data} {Hora}')
    print("")

print(f'{Nome}, VOCÊ QUER JOGAR UM JOGO?')
Resposta = input("Sim [Y]     Não [N]  ")

if Resposta == "Y" or Resposta == "y":
    print("ENTÃO VAMOS JOGAR HAHAHAHAHAHA")
elif Resposta == "N" or Resposta == "n":
    print("DESCULPE, MAS VAMOS JOGAR HAHAHAHAHAHA")
else:
    print(F"VOCÊ NÃO TEM ESCOLHA {Nome} HAHAHAHAHAHA")

print('O JOGO É JOKENPÔ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha_comp = randint(0,2)
rscolha_jogador = int(input('DIGITE A OPÇÃO DESEJADA: '))
