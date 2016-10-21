from  random import randint
jogador_1 =input("Qual o seu nome?")
print("Oi,",jogador_1, "o seu adversario eh o computador, PREPARE -SE!!\n As suas posicoes escolhidas sao marcadas com '0'.")
Matriz=[["-","-","-"],["-","-","-"],["-","-","-"]]
ja_jogados=[]
fimDeJogo = False
jogardor = "O"
computador = "x"
vencedor = ""
jogador_vencedor = ""

def imprime_Matriz(Matriz):
	for i in range(len(Matriz)):
		for j in range(len(Matriz[i])):
			print(Matriz[i][j])
		print()

	return Matriz

def copia_Matriz(Matriz):
	matrizCopia = []
	for i in Matriz:
		linhaCopia = []
		for j in i:
			linhaCopia.append(j)
		matrizCopia.append(copiaLinha)
	return matrizCopia


def verifica_Vencedor(Matriz):
	if Matriz[0][0] == "0" and Matriz[1][1] == "0" and Matriz[2][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[0][0] == '0' and Matriz[0][1] == '0' and Matriz[0][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[1][0] == '0' and Matriz[1][1] == '0' and Matriz[1][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[2][0] == '0' and Matriz[2][1] == '0' and Matriz[2][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[0][0] == '0' and Matriz[1][0] == '0' and Matriz[2][0] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[0][1] == '0' and Matriz[1][1] == '0' and Matriz[2][1] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[0][2] == '0' and Matriz[1][2] == '0' and Matriz[2][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[2][0] == '0' and Matriz[1][1] == '0' and Matriz[0][2] == "0":
		fimDeJogo = True
		vencedor = "O"
	elif Matriz[0][0] == 'x' and Matriz[1][1] == 'x' and Matriz[2][2] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[0][0] == 'x' and Matriz[0][1] == 'x' and Matriz[0][2] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[1][0] == 'x' and Matriz[1][1] == 'x' and Matriz[1][2] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[2][0] == 'x' and Matriz[2][1] == 'x' and Matriz[2][2] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[0][0] == 'x' and Matriz[1][0] == 'x' and Matriz[2][0] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[0][1] == 'x' and Matriz[1][1] == 'x' and Matriz[2][1] == "x":
		fimDeJogo = True
		vencedor = "x"
	elif Matriz[0][2] == 'x' and Matriz[1][2] == 'x' and Matriz[2][2] == "x":
		vencedor = "x"
	elif Matriz[2][0] == 'x' and Matriz[1][1] == 'x' and Matriz[0][2] == "x":
		vencedor = "x"


def jogador(Matriz):
	Posicao_jogada_linha_jogador1= int(input("Digite a posicao da linha que deseja jogar "+(jogador_1)+":"))
	Posicao_jogada_coluna_jogador1=int(input(" Digite a posicao da coluna que deseja jogar " +jogador_1+":"))
	if Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] =='-':
		Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] ='0'
	else:
		print("Essa posicao ja foi jogada!!")
		ja_jogados.append([Posicao_jogada_linha_jogador1,Posicao_jogada_coluna_jogador1])
		if Matriz[int(Posicao_jogada_linha_jogador1)][int(Posicao_jogada_coluna_jogador1)] == 'O':
			imprime_Matriz(Matriz)

def computador(Matriz):
	jogadas = [[], [], []]

	for i in range(3):
		for j in range(3):
			if Matriz[i][j] == "-":
				copiaMatriz = copia_Matriz(Matriz)
				copiaMatriz[i][j] = computador
				jogada = verifica_Jogada(Matriz, True)
				jogadas[jogada].append((i, j))

	if len(jogadas[0]):
		return jogadas[0][randint(0, len(jogadas[0])-1)]
	if len(jogadas[1]):
		return jogadas[1][randint(0, len(jogadas[1])-1)]
	if len(jogadas[2]):
		return jogadas[2][randint(0, len(jogadas[2])-1)]

def verifica_Jogada(Matriz, jogadaIA):
	jogadas = []

	if vencedor == computador:
		jogador_vencedor = "Computador"
	else:
		jogador_vencedor = jogador_1

	for i in range(3):
		for j in range(3):
			if Matriz[i][j]== "-":
				copiaMatriz = copia_Matriz(Matriz)
				if jogadaIA:
					copiaMatriz[i][j] = computador
				else:
					copiaMatriz[i][j] = jogador
				jogadas.append(verifica_Jogada(Matriz, False))

	if jogadas:
		if jogadaIA:
			jogadas = sorted(jogadas)
		else:
			jogadas = sorted(jogadas, reverse=True)
		return jogadas[0]
	return 1

while not fimDeJogo:
    jogador(Matriz)
    computador(Matriz, "X", "O")

print(jogador_vencedor, "ganhou o Jogo!!")
