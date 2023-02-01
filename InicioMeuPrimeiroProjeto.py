print("------------------------------------------------------------------------------------------------")
print("                               S U P E R   C A L C U L A D O R A                                ")
print("------------------------------------------------------------------------------------------------")
print("         |SOMA|SUBTRAÇÃO|DIVISÃO|MULTIPLICAÇÃO|RESTO DA DIVISÃO|RESULTADO PAR OU IMPAR|"         )
print("------------------------------------------------------------------------------------------------")

nome = input("Para utilizar a calculadora, digite seu nome: ")
print("Faaaaaaaaaaaaaaaaala. Eae ", nome , " tudo bem? espero que sim! ")
print("Bora utilizar minha super calculadora? Entao vamos lá.. ")
operacao = input("Escolha a operação desejada (soma, sub, div, mult, rest_div ) Para encerrar, digite sair : ")

while operacao != "sair":
    numero1 = input("Digite o primeiro número : ")
    numero2 = input("Digite o segundo número : ")
    if operacao == "soma":
        resultado = int(numero1) + int(numero2)
        print("O resultado da operação é: " + str(resultado))
    elif operacao == "sub":
        resultado = int(numero1) - int(numero2)
        print("O resultado da operação é: " + str(resultado))
    elif operacao == "div":
        resultado = int(numero1) / int(numero2)
        print("O resultado da operação é: " + str(resultado))
    elif operacao == "mult":
        resultado = int(numero1) * int(numero2)
        print("O resultado da operação é: " + str(resultado))
    elif operacao == "rest_div":
        resultado = int(numero1) % int(numero2)
        print("o resto da operação é :", resultado)
    if resultado % 2 ==0:
        print("o numero é par!")
    else:
        print("o numero é impar")

    print("------------------------------------------------------------------------------------------------")
    operacao = input("Escolha a operação desejada (soma, sub, div, mult, rest_div ) Para encerrar, digite sair : ")

if operacao == "sair":
    print("------------------------------------------------------------------------------------------------")
    print("                                          volte sempre                                          ")