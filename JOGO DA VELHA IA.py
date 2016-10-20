from  random import randint
jogador_1= input("Qual o seu nome?")
print("Oi,",jogador_1, "o seu adversário é o computador, PREPARE -SE!!\n As suas posições escolhidas são marcadas com '0'.")
Matriz=[["-","-","-"],["-","-","-"],["-","-","-"]]
jogo_finalizado= "Não"
jogadas_maquina=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
ja_jogados=[]

while True:

    def imprime_Matriz(Matriz):
        for i in range(len(Matriz)):
            for j in range(len(Matriz[i])):
                print(Matriz[i][j], end=" ")
            print()

        return Matriz  

    if Matriz[0][0] == '0' and Matriz[1][1] == '0' and Matriz[2][2] == "0":
        print(jogador_1,"ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[0][0] == '0' and Matriz[0][1] == '0' and Matriz[0][2] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[1][0] == '0' and Matriz[1][1] == '0' and Matriz[1][2] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[2][0] == '0' and Matriz[2][1] == '0' and Matriz[2][2] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[0][0] == '0' and Matriz[1][0] == '0' and Matriz[2][0] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[0][1] == '0' and Matriz[1][1] == '0' and Matriz[2][1] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[0][2] == '0' and Matriz[1][2] == '0' and Matriz[2][2] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[2][0] == '0' and Matriz[1][1] == '0' and Matriz[0][2] == "0":
        print(jogador_1,"Você ganhou o Jogo!! Parabéns!!")
        break
    elif Matriz[0][0] == 'x' and Matriz[1][1] == 'x' and Matriz[2][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[0][0] == 'x' and Matriz[0][1] == 'x' and Matriz[0][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[1][0] == 'x' and Matriz[1][1] == 'x' and Matriz[1][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[2][0] == 'x' and Matriz[2][1] == 'x' and Matriz[2][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[0][0] == 'x' and Matriz[1][0] == 'x' and Matriz[2][0] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[0][1] == 'x' and Matriz[1][1] == 'x' and Matriz[2][1] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[0][2] == 'x' and Matriz[1][2] == 'x' and Matriz[2][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break
    elif Matriz[2][0] == 'x' and Matriz[1][1] == 'x' and Matriz[0][2] == "x":
        print(" O computador ganhou o Jogo!!")
        break

    else:
        Posição_jogada_linha_jogador1= int(input("Digite a posição da linha que deseja jogar "+(jogador_1)+":"))
        Posição_jogada_coluna_jogador1=int(input(" Digite a posição da coluna que deseja jogar " +jogador_1+":"))
        if Matriz[int(Posição_jogada_linha_jogador1)][int(Posição_jogada_coluna_jogador1)] =='-':
            Matriz[int(Posição_jogada_linha_jogador1)][int(Posição_jogada_coluna_jogador1)] ='0'
            Matriz[int(Posição_jogada_linha_jogador1)-1][int(Posição_jogada_coluna_jogador1)+1] = 'x'
        else:
            print("Essa posição já foi jogada!!")
        ja_jogados.append([Posição_jogada_linha_jogador1,Posição_jogada_coluna_jogador1])
        if Matriz[int(Posição_jogada_linha_jogador1)][int(Posição_jogada_coluna_jogador1)] == 'x' or Matriz[int(Posição_jogada_linha_jogador1)][int(Posição_jogada_coluna_jogador1)]=="0":
            imprime_Matriz(Matriz)
