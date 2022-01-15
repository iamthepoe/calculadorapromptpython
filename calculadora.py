import os
import math
clear = lambda: os.system('cls')
escolheuSair = False

def Somar(x,y):
	print(f'{x} + {y} = {x+y}')

def Subtrair(x,y):
	print(f'{x} - {y} = {x-y}')

def Dividir(x,y):
	print(f'{x} / {y} = {x/y}')

def Multiplicar(x,y):
	print(f'{x} x {y} = {x*y}')

def RaizQuadrada(x):
	print(f'{math.sqrt(x)}')

def Tabuada(x):
	for n in range(1, 11, 1):
		print(f'{x} x {n} = {x*n}')

def ContinuarPrograma(msg):
	let = input(msg)
	clear()


while not escolheuSair:
	opcao = int(input("[1] - Somar\n[2] - Subtrair\n[3] - Dividir\n[4] - Multiplicar\n[5] - Raíz quadrada\n[6] - Tabuada\n[0] - Sair\n"))
	clear
	if opcao<0 and opcao>6:
		ContinuarPrograma("Essa opção não existe! Pressione ENTER para CONTINUAR");		
	elif opcao==0:
		escolheuSair = True;
	elif opcao==1:
		n1 = int(input("Insira o 1° valor: "))
		n2 = int(input("Insira o 2° valor: "))
		Somar(n1,n2)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	elif opcao==2:
		n1 = int(input("Insira o 1° valor: "))
		n2 = int(input("Insira o 2° valor: "))
		Subtrair(n1,n2)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	elif opcao==3:
		n1 = int(input("Insira o 1° valor: "))
		n2 = int(input("Insira o 2° valor: "))
		Dividir(n1,n2)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	elif opcao==4:
		n1 = int(input("Insira o 1° valor: "))
		n2 = int(input("Insira o 2° valor: "))
		Multiplicar(n1,n2)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	elif opcao==5:
		n1 = int(input("Insira o valor: "))
		RaizQuadrada(n1)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	else:
		n1 = int(input("Insira o valor: "))
		Tabuada(n1)
		ContinuarPrograma("\nPressione ENTER para CONTINUAR\n")
	