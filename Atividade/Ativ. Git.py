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

while True:
    print('O JOGO É JOKENPÔ')
    print('[ 0 ] PEDRA')
    print('[ 1 ] PAPEL')
    print('[ 2 ] TESOURA')
    Computador = randint(0,2)
    Jogador = int(input('DIGITE A OPÇÃO DESEJADA: '))

    # ESCOLHA MAQUINA
    if Computador == 0:
        print("___________________________________")
        print("O COMPUTADOR ESCOLHEU PEDRA")
    elif Computador == 1:
        print("___________________________________")
        print("O COMPUTADOR ESCOLHEU PAPEL")
    else:
        print("___________________________________")
        print("O COMPUTADOR ESCOLHEU TESOURA")

    # ESCOLHA JOGADOR
    if Jogador == 0:
        print("O JOGADOR ESCOLHEU PEDRA")
        print("___________________________________")
        print("")
    elif Jogador == 1:
        print("O JOGADOR ESCOLHEU PAPEL")
        print("___________________________________")
        print("")
    else:
        print("O JOGADOR ESCOLHEU TESOURA")
        print("___________________________________")
        print("")


    if Computador == Jogador:
        print("O AMBOS ESCOLHERAM A MESMA OPÇÃO O JOGO EMPATOU!")

    elif Computador == 0 and Jogador == 1:
        print(f"vOCÊ GANHOU {Nome} :( ")
    elif Computador == 2 and Jogador == 0:
        print(f"vOCÊ GANHOU {Nome} :( ")
    elif Computador == 1 and Jogador == 2:
        print(f"vOCÊ GANHOU {Nome} :( ")

    else: 
        print(f"VOCÊ PERDEU {Nome} MUITO RUIM HAHAHAHAHAHAHA!")

    print("QUER PARAR? ")
    Resposta_2 = input("Sim [Y]     Não [N]  ")

    if Resposta_2 == "Y" or Resposta_2 == "y":
        break