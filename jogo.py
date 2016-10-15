
Jogador_1= input("Digite o nome do jogador 1:")
Jogador_2= input("Digite o nome do jogador 2:")
jogadorVencedor = ""
jogo_finalizado= "Não"

matriz=[["-","-","-"],["-","-","-"],["-","-","-"]]

def imprime_matriz(matriz):
	for i in range (len(matriz)):
		for j in range (len(matriz[i])):
			print(matriz[i][j], end= " ")
		print()

imprime_matriz(matriz)

while jogo_finalizado=="Não":
	
	if matriz[0][0]== "o" and matriz[0][1]== "o" and matriz[0][2] == "o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break
	
	elif matriz[1][0]== "o" and matriz[1][1]== "o" and matriz[1][2]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break 
	
	elif matriz[2][0]== "o" and matriz[2][1]== "o" and matriz[2][2]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break		
	
	elif matriz[0][0]== "o" and matriz[1][0]== "o" and matriz[2][0]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break
	
	elif matriz[0][1]== "o" and matriz[1][1]== "o" and matriz[2][1]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break
	
	elif matriz[0][2]== "o" and matriz[1][2]== "o" and matriz[2][2]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break
	
	elif matriz[0][0]== "o" and matriz[1][1]== "o" and matriz[2][2]=="o":
		jogadorVencedor = Jogador_1
		jogo_finalizado="sim"
		break
	
	elif matriz[0][2]== "o" and matriz[1][1]== "o" and matriz[2][0]=="o":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[0][0]== "x" and matriz[0][1]== "x" and matriz[0][2]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[1][0]== "x" and matriz[1][1]== "x" and matriz[1][2]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[2][0]== "x" and matriz[2][1]== "x" and matriz[2][2]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break		
	
	elif matriz[0][0]== "x" and matriz[1][0]== "x" and matriz[2][0]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[0][1]== "x" and matriz[1][1]== "x" and matriz[2][1]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[0][2]== "x" and matriz[1][2]== "x" and matriz[2][2]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[0][0]== "x" and matriz[1][1]== "x" and matriz[2][2]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	elif matriz[0][2]== "x" and matriz[1][1]== "x" and matriz[2][0]=="x":
		jogadorVencedor = Jogador_2
		jogo_finalizado="sim"
		break
	
	else:
	
		posicao_linha_jogador_1= int(input("Digite a linha que deseja jogar "+Jogador_1+":"))
		posicao_coluna_jogador_1= int(input("Digite a coluna que deseja jogar "+Jogador_1+":"))
		
		if matriz[int(posicao_linha_jogador_1)][int(posicao_coluna_jogador_1)]=="-" and jogo_finalizado=="Não":
			matriz[posicao_linha_jogador_1][posicao_coluna_jogador_1]="o"
			imprime_matriz(matriz)
		
		posicao_linha_jogador_2=int(input("Digite a linha que deseja jogar "+ Jogador_2+":"))
		posicao_coluna_jogador_2=int(input("Digite a coluna que deseja jogar "+ Jogador_2+":"))
		
		if matriz[int(posicao_linha_jogador_2)][int(posicao_coluna_jogador_2)]=="-" and jogo_finalizado=="Não":
			matriz[posicao_linha_jogador_2][posicao_coluna_jogador_2]="x"
			imprime_matriz(matriz)
		
		else:
			break
		
print("Parabéns "+ jogadorVencedor+" você venceu o jogo!!")
	