Nome = input("Insira seu Nome: ")
idade = int(input('digite sua idade: '))
Hora = input("Informe a hora atual: ")

if Hora <= "12:00":
    print (f"Bom Dia! {Nome}, sua idade atual é {idade}anos e a hora é {Hora}")
elif Hora <= "18:00":
    print (f"Boa Tarde! {Nome}, sua idade atual é {idade} anos e a hora é {Hora}")
else: 
    print (f"Boa Noite! {Nome}, sua idade atual é {idade} anos e a hora é {Hora}")
    
