import random, server


Matriz = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
ja_jogados = []
fimDeJogo = False
jogador1 = "O"
jogador2 = "x"
vencedor = ""
jogador_vencedor = ""
empate = False



def menu():
    print("Modo de Jogo")
    print("1 - Offline (Player vs PC)")
    print("2 - Online (Player vs Player)")
    modoJogo = int(raw_input())
    if modoJogo == 1:
    	offline()
    elif modoJogo == 2:
    	online()


def imprime_Matriz(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            print(Matriz[i][j]),
        print ""
    return Matriz


def verifica_Vencedor(Matriz):
    if Matriz[0][0] == Matriz[1][1] == Matriz[2][2] == "0":
        return jogador1
    elif Matriz[0][0] == '0' and Matriz[0][1] == '0' and Matriz[0][2] == "0":
        return jogador1
    elif Matriz[1][0] == '0' and Matriz[1][1] == '0' and Matriz[1][2] == "0":
        return jogador1
    elif Matriz[2][0] == '0' and Matriz[2][1] == '0' and Matriz[2][2] == "0":
        return jogador1
    elif Matriz[0][0] == '0' and Matriz[1][0] == '0' and Matriz[2][0] == "0":
        return jogador1
    elif Matriz[0][1] == '0' and Matriz[1][1] == '0' and Matriz[2][1] == "0":
        return jogador1
    elif Matriz[0][2] == '0' and Matriz[1][2] == '0' and Matriz[2][2] == "0":
        return jogador1
    elif Matriz[2][0] == '0' and Matriz[1][1] == '0' and Matriz[0][2] == "0":
        return jogador1
    elif Matriz[0][0] == 'x' and Matriz[1][1] == 'x' and Matriz[2][2] == "x":
        return jogador2
    elif Matriz[0][0] == 'x' and Matriz[0][1] == 'x' and Matriz[0][2] == "x":
        return jogador2
    elif Matriz[1][0] == 'x' and Matriz[1][1] == 'x' and Matriz[1][2] == "x":
        return jogador2
    elif Matriz[2][0] == 'x' and Matriz[2][1] == 'x' and Matriz[2][2] == "x":
        return jogador2
    elif Matriz[0][0] == 'x' and Matriz[1][0] == 'x' and Matriz[2][0] == "x":
        return jogador2
    elif Matriz[0][1] == 'x' and Matriz[1][1] == 'x' and Matriz[2][1] == "x":
        return jogador2
    elif Matriz[0][2] == 'x' and Matriz[1][2] == 'x' and Matriz[2][2] == "x":
        return jogador2
    elif Matriz[2][0] == 'x' and Matriz[1][1] == 'x' and Matriz[0][2] == "x":
        return jogador2
    else:
	for i in range(3):
		for j in range(3):
			if Matriz[i][j] != '-':
				empate = True
			else:
				empate = False
				break
	return empate


def online():

	fimDeJogo = False

	print("Modo de Rede")
	print("1 - Server")
	print("2 - Client")
	modoRede = int(raw_input())

	def get_pos1():
		return str(Posicao_jogada_linha_jogador1+Posicao_jogada_coluna_jogador1)
	def get_pos2():
		return str(Posicao_jogada_linha_jogador2+Posicao_jogada_coluna_jogador2)

	def server():

		def jogador1(Matriz):
		    Posicao_jogada_linha_jogador1= int(input("Digite a posicao da linha que deseja jogar :"))
		    Posicao_jogada_coluna_jogador1=int(input("Digite a posicao da coluna que deseja jogar :"))
		    if Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] == '-' :
		        Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] = "O"
		    else:
		        print("Essa posicao ja foi jogada!!")
		        ja_jogados.append([Posicao_jogada_linha_jogador1,Posicao_jogada_coluna_jogador1])

		jogador1(Matriz)

	def client():

		def jogador2(Matriz):
		    Posicao_jogada_linha_jogador2= int(input("Digite a posicao da linha que deseja jogar :"))
		    Posicao_jogada_coluna_jogador2=int(input("Digite a posicao da coluna que deseja jogar :"))
		    if Matriz[int(Posicao_jogada_linha_jogador2)][int(Posicao_jogada_coluna_jogador2)] == '-' :
		        Matriz[int(Posicao_jogada_linha_jogador2)][int(Posicao_jogada_coluna_jogador2)] = "x"
		    else:
		        print("Essa posicao ja foi jogada!!")
		        ja_jogados.append([Posicao_jogada_linha_jogador2,Posicao_jogada_coluna_jogador2])

		jogador2(Matriz)

	while (fimDeJogo == False):
		if modoRede == 1:
			server()
		else:
			client()

		if verifica_Vencedor(Matriz) == jogador2:
			fimDeJogo = True
			print ('Jogador 2 venceu o jogo!')
		if verifica_Vencedor(Matriz) == jogador1:
			fimDeJogo = True
			print ('Jogador 1 venceu o jogo!')
		if verifica_Vencedor(Matriz) == empate == True:
			print ('O jogo empatou!')
		imprime_Matriz(Matriz)


def offline():

	fimDeJogo = False


	def copia_Matriz(Matriz):
	    matrizCopia = []
	    for i in Matriz:
	        linhaCopia = []
	        for j in i:
	            linhaCopia.append(j)
	        matrizCopia.append(linhaCopia)
	    return matrizCopia


	def jogador(Matriz):
	    Posicao_jogada_linha_jogador1= int(input("Digite a posicao da linha que deseja jogar :"))
	    Posicao_jogada_coluna_jogador1=int(input("Digite a posicao da coluna que deseja jogar :"))
	    if Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] == '-' :
	        Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] = "0"
	    else:
	        print("Essa posicao ja foi jogada!!")
	        ja_jogados.append([Posicao_jogada_linha_jogador1,Posicao_jogada_coluna_jogador1])


	#Algoritmo MinMax - Desenvolvido por Gustavo Vilar ( github.com/gvilardefarias )

	def computador(Matriz):
	    jogadas = [[], [], []]

	    for i in range(3):
	        for j in range(3):
	            if Matriz[i][j] == "-":
	                copiaMatriz = copia_Matriz(Matriz)
	                copiaMatriz[i][j] = computador
	                jogada = verifica_Jogada(Matriz)
	                jogadas[jogada].append((i, j))

	    if len(jogadas[0]):
	        a = jogadas[0][random.randint(0, len(jogadas[0])-1)][0]
	        b = jogadas[0][random.randint(0, len(jogadas[0])-1)][1]
	        if Matriz[a][b] == '-':
	            Matriz[a][b] = 'x'
	    if len(jogadas[1]):
	        a = jogadas[1][random.randint(0, len(jogadas[1])-1)][0]
	        b = jogadas[1][random.randint(0, len(jogadas[1])-1)][1]
	        if Matriz[a][b] == '-':
	            Matriz[a][b] = 'x'
	    if len(jogadas[2]):
	        a = jogadas[2][random.randint(0, len(jogadas[2])-1)][0]
	        b = jogadas[2][random.randint(0, len(jogadas[2])-1)][1]
	        if Matriz[a][b] == '-':
	            Matriz[a][b] = 'x'


	def verifica_Jogada(Matriz, vez=0):
	    jogadas = []
	    vencedor = verifica_Vencedor(Matriz)

	    if vencedor == computador:
	        return 0
	    else:
	        return 2

	    for i in range(3):
	        for j in range(3):
	            if Matriz[i][j] == "-":
	                copiaMatriz = copia_Matriz(Matriz)
	                if vez % 2:
	                    copiaMatriz[i][j] = computador
	                else:
	                    copiaMatriz[i][j] = jogador
	                jogadas.append(verifica_Jogada(Matriz, vez+1))

	    if jogadas:
	        if vez % 2:
	            jogadas = sorted(jogadas)
	        else:
	            jogadas = sorted(jogadas, reverse=True)
	        return jogadas[0]

	    return 1
	#Algoritmo MinMax - Desenvolvido por Gustavo Vilar ( github.com/gvilardefarias )

	while (fimDeJogo == False):
		jogador(Matriz)
		computador(Matriz)
		if verifica_Vencedor(Matriz) == jogador2:
			fimDeJogo = True
			print ('Jogador 2 venceu o jogo!')
		if verifica_Vencedor(Matriz) == jogador1:
			fimDeJogo = True
			print ('Jogador 1 venceu o jogo!')
		if verifica_Vencedor(Matriz) == empate == True:
			print ('O jogo empatou!')
		imprime_Matriz(Matriz)



menu()
