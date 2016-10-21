import random 
jogador_1 = raw_input("Qual o seu nome?")
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
        print ""        
    return Matriz
 
def copia_Matriz(Matriz):
    matrizCopia = []
    for i in Matriz:
        linhaCopia = []
        for j in i:
            linhaCopia.append(j)
        matrizCopia.append(linhaCopia)
    return matrizCopia
 
 
def verifica_Vencedor(Matriz):
    if Matriz[0][0] ==  Matriz[1][1] ==  Matriz[2][2] == "0":
        return jogador
    elif Matriz[0][0] == '0' and Matriz[0][1] == '0' and Matriz[0][2] == "0":
        return jogador
    elif Matriz[1][0] == '0' and Matriz[1][1] == '0' and Matriz[1][2] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[2][0] == '0' and Matriz[2][1] == '0' and Matriz[2][2] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[0][0] == '0' and Matriz[1][0] == '0' and Matriz[2][0] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[0][1] == '0' and Matriz[1][1] == '0' and Matriz[2][1] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[0][2] == '0' and Matriz[1][2] == '0' and Matriz[2][2] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[2][0] == '0' and Matriz[1][1] == '0' and Matriz[0][2] == "0":
        fimDeJogo = True
        return jogador
    elif Matriz[0][0] == 'x' and Matriz[1][1] == 'x' and Matriz[2][2] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[0][0] == 'x' and Matriz[0][1] == 'x' and Matriz[0][2] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[1][0] == 'x' and Matriz[1][1] == 'x' and Matriz[1][2] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[2][0] == 'x' and Matriz[2][1] == 'x' and Matriz[2][2] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[0][0] == 'x' and Matriz[1][0] == 'x' and Matriz[2][0] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[0][1] == 'x' and Matriz[1][1] == 'x' and Matriz[2][1] == "x":
        fimDeJogo = True
        return computador
    elif Matriz[0][2] == 'x' and Matriz[1][2] == 'x' and Matriz[2][2] == "x":
        return computador
    elif Matriz[2][0] == 'x' and Matriz[1][1] == 'x' and Matriz[0][2] == "x":
        return computador
 
 
def jogador(Matriz):
    Posicao_jogada_linha_jogador1= int(input("Digite a posicao da linha que deseja jogar "+(jogador_1)+":"))
    Posicao_jogada_coluna_jogador1=int(input("Digite a posicao da coluna que deseja jogar " +jogador_1+":"))
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
                 
    print jogadas
                 
    if len(jogadas[0]):
        a = jogadas[0][randint(0, len(jogadas[0])-1)][0]
        b = jogadas[0][randint(0, len(jogadas[0])-1)][1]
        Matriz[a][b] = 'x'
    if len(jogadas[1]):
        a = jogadas[1][randint(0, len(jogadas[1])-1)][0]
        b = jogadas[1][randint(0, len(jogadas[1])-1)][1]
        Matriz[a][b] = 'x'
    if len(jogadas[2]):
        a = jogadas[2][random.randint(0, len(jogadas[2])-1)][0]
        b = jogadas[2][random.randint(0, len(jogadas[2])-1)][1]
        print a 
        print b
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
            if Matriz[i][j]== "-":
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
    imprime_Matriz(Matriz)
     
    if verifica_Vencedor(Matriz) == computador :
        fimDeJogo = True
        jogador_vencedor = 'Computador'
    if verifica_Vencedor(Matriz) == jogador:
        fimDeJogo = True
        jogador_vencedor = jogador_1
         
 
print(jogador_vencedor, 'ganhou o Jogo!!')
