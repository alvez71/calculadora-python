import os
import time

while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  print("--------------------CALCULADORA DO ALVES--------------------")
  print("Qual operação matemática você quer fazer?")
  print("1. Soma")
  print("2. Multiplicação")
  print("3. Divisão")
  print("4. Subtração")
  opcao = input("Escolha uma das 4 opções: ")
  if opcao == "1":
    print("Perfeito, vamos somar!")
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    resultado = n1 + n2
    print(f"A soma de \033[31m{n1}\033[m + \033[31m{n2}\033[m é igual à \033[32m{resultado}\033[m")
    
    print("\nRetornando ao menu em \033[33m3 segundos\033[m")
    time.sleep(3)
  elif opcao == "2":
    print("Perfeito, vamos multiplicar!")
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    resultado = n1 * n2
    print(f"A multiplicação de \033[31m{n1}\033[m x \033[31m{n2}\033[m é igual à \033[32m{resultado}\033[m")
    
    print("\nRetornando ao menu em \033[33m3 segundos\033[m")
    time.sleep(3)
  elif opcao == "3":
    print("Perfeito, vamos dividir!")
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    if n2 == 0:
      print("ERROR: Não é possivel dividir por zero!")
      print("\nRetornando ao menu em \033[33m3 segundos\033[m")
      time.sleep(3)
    else:
      resultado = n1 / n2
      print(f"A divisão de \033[31m{n1}\033[m ÷ \033[31m{n2}\033[m é igual \033[32m{resultado}\033[m")
      time.sleep(3)
      
  elif opcao == "4":
    print("Perfeito, vamos subtrair!")
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    resultado = n1 - n2
    print(f"A subtração de \033[31m{n1}\033[m - \033[31m{n2}\033[m é igual à \033[32m{resultado}\033[m")
    
    print("\nRetornando ao menu principal em \033[33m3 SEGUNDOS...\033[m")
    time.sleep(3)