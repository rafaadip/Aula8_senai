### ACESSANDO TUPLAS
# numeros = (1,2,3,4,5)
# lista_de_numeros = list(numeros)
# print("Lista de números:",lista_de_numeros)
# ### metodo list()
# tuple1 = (2,234,567,444,777)
# print(tuple1)
# transform = list(tuple1)
# print(transform)

# 1 -  Crie uma tupla chamada `frutas` com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla. 
# tupla = ('Maçã','Pêra','Abacaxi','Banana')
# print(tupla[2])

# 2 - Crie uma tupla chamada `numeros` com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.
# numeros = (1,2,3,4)
# lista = list(numeros)
# print(lista)

# 3 - Crie uma tupla chamada `meses` com os nomes dos meses do ano até Setembro. Use um loop `for` para imprimir cada mês em uma linha separada.
# meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Agosto','Setembro')
# for mes in meses:
#     print(mes)

# 4 - Crie uma lista chamada `notas` com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.

# notas = [100 ,20,3,4,5,6,7,8,9]
# tupla = (notas)
# print(tupla)

# 5 - Crie uma lista chamada `ponto` que represente as coordenadas (x, y) de um ponto. Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.

# ponto = ['1213','34345']
# x,y = ponto
# print(f"Os valores desempacotados, são respectivamente {x} e {y}")

### Exemplos de função
# def soma():
#     a = 15
#     b = 10
#     print(a + b)
# soma()

# def cumprimento():
#     nome = input("Digite o seu nome: ")
#     idade = input("Digite a sua idade: ")
#     print(f'O nome do usuário é {nome} a idade é {idade}')
# cumprimento()

# def subtracao():
#     a = int(input("Digite um numero aqui: "))
#     b = int(input("Digite outro número aqui: "))
#     resultado = a - b
#     print(resultado)
# subtracao()

### CALCULADORA
# def calculadora():
#     a = float(input("Digite um número aqui: "))
#     b = float(input("Digite um outro número aqui: "))
#     somaN = int(a+b) 
#     subN = int(a-b)
#     multN = int(a*b)
#     divideN = int(a/b)
#     print("A soma desse número é: ", somaN)
#     print("A subtração desse número é: ", subN)
#     print("A multiplicação desse número é: ", multN)
#     print("A divisão é: ", divideN)
# calculadora()
# def calculadora2 ():
#     n1 = float(input("Digite um número aqui: "))
#     operacao = input("Digite a operação desejada dentro do (), Subtração(-), Divisão(/), Multiplicação(*), Adição(+): ")
#     n2 = float(input("Digite outro número aqui: "))
    
# def calculadora2():
#     n1 = float(input("Digite um número aqui: "))
#     operacao = input("Digite a operação desejada dentro do (), Subtração(-), Divisão(/), Multiplicação(*), Adição(+): ")
    
#     if operacao not in ["-", "+", "/", "*"]:
#         print("Insira uma operação válida!")
#     else:
#         n2 = float(input("Digite outro número aqui: "))
#         if operacao == "-":
#             print(f'{n1} - {n2} = {n1 - n2}')
#         elif operacao == "+":
#             print(f'{n1} + {n2} = {n1 + n2}')
#         elif operacao == "/":
#             if n2 == 0:
#                 print("Erro! Divisão por zero não é permitida.")
#             else:
#                 print(f'{n1} / {n2} = {n1 / n2}')
#         elif operacao == "*":
#             print(f'{n1} * {n2} = {n1 * n2}')

# calculadora2()
