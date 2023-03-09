#Felipe Peixoto de Oliveira
def ImagemJogo () :
    global jogo
    global turno
    print ("")
    print ("     ",vitorias_o,"            x           ",vitorias_x)
    print ("             " + "  A    B    C  ")
    linhas = ["","",""]
    for i in range (3) :
        #esquerda
        linhas [i] = ImagemJogoHud (i, linhas[i], False)
        linhas [i] += str(i + 1)
        for j in range (3) :
            num = jogo[i][j]
            char = ""
            if (num == -1) :
                char = "O"
            else :
                if (num == 1) :
                    char = "X"
                else :
                    if (num == 2) :
                        letter = ""
                        if (turno == -1) :
                            letter ="X"
                        else :
                            letter ="O"
                        char = "\033[92m" + letter + "\033[0m"
                    else :
                        char = " "
            if j == 1 :
                linhas [i] += " | " + char + " | "
            else :
                linhas [i] += " " + char + " "
        #if i != 2 :
            #linhas[i] = "\u0332".join(linhas[i])
                #esquerda
        linhas [i] = ImagemJogoHud (i, linhas[i], True)
        print (linhas [i])

def ImagemJogoHud (i, linha, x) :
    global vitoria
    global TurnoNumero
    global turno
    global vitorias_o
    global vitorias_x
    TurnodoJogador = False

    if (turno == 1 and x == True) or (turno == -1 and x == False) :
        TurnodoJogador = True
    else :
        TurnodoJogador = False

    if (i == 0) :
        if (x == True) :
            linha += "      X      "
        else :
            linha += "      O      "
    else :
        if (i == 1) :
            if (vitoria == True) :
                if (TurnodoJogador) :
                    linha += "\033[91m" + "   DERROTA   " + "\033[0m"
                else :
                    linha += "\033[92m" + "   VITÓRIA   " + "\033[0m"
                    if (x == True) :
                        vitorias_x += 1
                    else :
                        vitorias_o += 1
            else :
                if (TurnoNumero == 9) :
                    if (x == True) :
                        linha += "\033[93m" + "    VELHA    " + "\033[0m"
                    else :
                        linha += "\033[93m" + "     DEU     " + "\033[0m"
                else :
                    if (TurnodoJogador) :
                        linha += "      ^      "
                    else :
                        linha += "             "
        else :
            linha += "             "
    return (linha)

def ColorirVencedor (diagonal, linha, coluna) :
    #0 = diagonal | 1 = diagonal inv 
    global jogo
    global vitoria
    global FimJogo
    FimJogo = True
    vitoria = True
    if diagonal != -1 :
        for i in range (3) :
            if (diagonal == 0) :
                jogo[i][i] = 2
            else :
                if (diagonal == 1) :
                    jogo[i][2-i] = 2
    else :
        for j in range (3) :
            if (linha != -1) :
                jogo[linha][j] = 2
            else :
                jogo[j][coluna] = 2            
        

def verificar_numero (valor) :
    resultado = True
    try:
        valor = int(valor)
    except ValueError:
        resultado = False
    return resultado

def DesignarValor (char, char2) :
    global coluna
    global linha
    if (verificar_numero (char)) :
        linha = char
        coluna = char2
    else :
        coluna = char
        linha = char2

#status do jogo
vitorias_x = 0
vitorias_o = 0
jogando = True
while (jogando == True) :
    #status da partida
    turno = 1
    TurnoNumero = 0
    jogo = [[0,0,0],[0,0,0],[0,0,0,]]
    posAnteriores = []
    coluna = -1
    linha = -1
    FimJogo = False
    vitoria = False

    #jogo
    ImagemJogo ()
    while (FimJogo == False) :
        escolha = input ("Escolha uma posição número/letra: ")

        #validar escolhar
        valido = False
        while (valido == False) :
            if (len(escolha) == 2) :
                #Designar valores
                DesignarValor (escolha [0], escolha [1])
                linhaNum = verificar_numero (linha)
                colunaNum = verificar_numero (coluna)
                if colunaNum and linhaNum :
                    print ("Digite uma letra")
                else :
                    if linhaNum == False and colunaNum == False :
                        print ("Digite um número")
                    else :
                        linha = int (linha)
                        coluna = coluna.upper ()
                        if linha > 0 and linha < 4 :
                            if coluna == "A" or coluna == "B" or coluna == "C" :
                                ColunaPosReal = ["A", "B", "C"]
                                #Acertar posição e verificar se já foi selecionada
                                for i in range (3) :
                                    if (ColunaPosReal [i] == coluna) :
                                        coluna = int (i)
                                linha -= 1
                                posRepetida = False
                                posFinal = str (linha) + str (coluna)
                                for i in posAnteriores :
                                    if i == posFinal :
                                        posRepetida = True
                                if posRepetida == True :
                                    print ("Essa posição já foi preenchida")
                                else :
                                    posAnteriores.append (posFinal)
                                    valido = True
                            else :
                                print ("Digite uma letra válida")
                        else :
                            print ("Digite um número válido")
            else :
                print ("Digite um número e uma letra")
            if (valido == False) :
                escolha = input("Escolha uma posição válida: ")
        
        #jogar
        jogo [linha][coluna] = turno

        #Trocar turno
        if turno == 1 :
            turno = -1
        else :
            turno = 1

        ImagemJogo ()

        #Verificar vitória
        somaDiagonal = 0
        somaDiagonalIn = 0
        for i in range(3) :
            somaDiagonal += jogo[i][i]
            somaDiagonalIn += jogo[i][2-i]
            somaHorizontal = 0
            somaVertical = 0
            for j in range(3) :
                somaHorizontal += jogo[i][j]
                somaVertical += jogo[j][i]
            if (somaHorizontal == 3 or somaHorizontal == -3) :
                ColorirVencedor (-1, i, -1)
                break
            if (somaVertical == 3 or somaVertical == -3) :
                ColorirVencedor (-1, -1, i)
                break
        if (somaDiagonal == 3 or somaDiagonal == -3) :
            ColorirVencedor (0, -1, -1)
            break
        if (somaDiagonalIn == 3 or somaDiagonalIn == -3) :
            ColorirVencedor (1, -1, -1)
            break
            
        TurnoNumero += 1
        if TurnoNumero == 9 :
            FimJogo = True
        
    print ("")
    ImagemJogo ()
    op = input ("Digite S para continuar jogando")
    if (op.upper() != "S") :
        jogando = False
  
