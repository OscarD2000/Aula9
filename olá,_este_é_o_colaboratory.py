# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Nova seção
"""

def display(name):
    print('ola', name)

display('oscar')
display('julia')
display('fernando')

name4 = 'caio'
def display():
    name ='julia'
    namw2 = 'fernando'
    name3 = 'carlos'
    print('ola', name)
    print('ola', name2)
    print('ola', name3)
    print('ola', name4)

def soma():
  n = int(input('digite um numero'))
  x = int(input('digite um numero'))
print(n+x)

soma()

frutas = ('morango','maçã','uva','abacaxi','abacate')
index = (frutas[2])
print(index)

numeros = (5,8,7,12)
lista = list(numeros)
print(lista)

meses = ('jan','fev','mar','abr','mai','jun','jul','ago','set')
for i in meses:
  print(i)

notas = (10,7,5,12)
tuple = tuple(notas)
print(tuple)

ponto = [10,20]
x, y = ponto
print('coordenada x', x)
print('coordenada y', y)

def calculadora():
    x = float(input('digite um numero'))
    y = float(input('digite um numero'))
    print(x*y)
    print(x+y)
    print(x-y)
    print(x/y)

calculadora()

def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a opção (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida")


calculadora()

prato = 'vazio'
copo = 'vazio'
def pratos():
  print(f'digite - 1(Pizza) 2(Macarronada) 3(Lanche)')
  escolha = input('Digite sua opção:')
  if escolha == '1':
     prato = 'você escolheu pixxa'
  elif escolha == '2' :
       prato = 'você escolheu macarronada'
       print(prato)
  else:
       prato = 'você escolheu lanche'
       print(prato)

x = isinstance(2.5, int)
print(x)

x = isinstance(2, int)
print(x)

dictin = {
  'key': 'value1',
  'key2': 'value2',
  'key3': 3,
  'key4':True,
  'key5': 5.5

}

notas_declaradas ={
"José": 9,
"Maria": 10,
"Felipe":7
}

c = 10

while c <=10:
    nome_que_vai_entrar = input("digite o nome do aluno >> ")
    nota = float(input("Digite a nota do aluno >> "))


    if notas_declaradas.get(nome_que_vai_entrar):
        print("Já existe o aluno", nome_que_vai_entrar)
    else:
        notas_declaradas[nome_que_vai_entrar] = nota
        print(notas_declaradas)

for chave, valor in my_dict.items():
    print(f'{chave}: {valor}')

dicionario = {
    "feliz": "contente",
    "triste": "desanimado",
    "bonito": "belo",
    "pobre": "necessitado",
    "rico": "próspero"
}
palavra = input("digite uma palavra: ")
if palavra in dicionario:
    sinonimo = dicionario[palavra]
    print(f"sinônimo de {palavra}: {sinonimo}")
else:
    print("essa palavra não está no dicionário.")

dicionário = {0:'A',1:'E', 2:'I',3:'O',4:'U'}
indice = dicionário[2]
print(indice)

def soma_lista(lista):
      soma = 0
    for numero in lista:
        soma += numero
        return soma

def soma (n):
    soma = 0
    for i in range(1,n + 1):
        soma += i
    return soma

n = 10
resultado = soma(n)
print(f'a soma dos numeros de 1 a(n) é {resultado}')

def contar_letra(letra, palavra):
    cont = 0
    for char in palavra:
        if char == letra:
            cont += 1
    return cont
palavra = "macarronada"
letra = "a"
resultado = contar_letra(letra, palavra)
print(f"A letra '{letra}' aparece {resultado} vezes na palavra '{palavra}'.")

def calcular(N):
    if N < 0:
        return "O fatorial não está definido para números negativos."
    elif N == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, N + 1):
            fatorial *= i
        return fatorial
N = 5
resultado = calcular(N)
print(f"O fatorial de {N} é {resultado}")

dicionário = {'1,g,5,45,88,p'}
print(dicionário)

for i in range(3)
mecadoria = input('Insira três produtos')
preco = float(input(f'insira o preço do {mercadoria}: R$ '))
produtos[mercadoria] = preco

print(' Lista de produtos e preços':')
for