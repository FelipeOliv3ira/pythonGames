#Felipe Peixoto de Oliveira - Engenharia de Software
import random
import time

def RetornarAlfabeto () :
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def CriarMatriz (largura) :
    matriz = []
    for i in range (largura) :
        linha = []
        for i in range (largura) :
            linha.append (0)
        matriz.append (linha)
    return matriz

def verificar_numero (valor) :
    resultado = True
    try:
        valor = int(valor)
    except ValueError:
        resultado = False
    return resultado

def DigitarNumLetra () :
    coluna = 0
    linha = 0
    print ("Digite uma letra: ")
    linha = ValorIgualLista (verificar_resposta (1).upper (), RetornarAlfabeto ())
    print ("Digite um número: ")
    coluna = int (verificar_resposta (0)) - 1
    return [linha, coluna]

def ValorIgualLista (valor, vetor) :
    i = 0
    encontrado = False
    while (encontrado == False) :
        if (i > len (vetor) - 1) :
            encontrado = True
        else :
            if (vetor [i] == valor) :
                encontrado = True
            else :
                i += 1
    return i

def ApresentarJogo (matriz, assist) :
    nums = "  "
    for j in range (len (matriz)) :
        if (j > 9) :
            nums += " " + str(j + 1)
        else :
            nums += " " + str(j + 1) + " "
    print (nums)
    for i in range (len (matriz)) :
        linha = ""
        alfabeto = RetornarAlfabeto ()      
        linha1 = CriarLinha (matriz, i, assist)
        linha += alfabeto [i] + " " + linha1 
        print (linha)

def CriarLinha (matriz, i, assist) :
    linha = ""
    for j in range (len (matriz)) :
        valor = matriz [i][j]
        if (valor == 0) :
            linha += "\033[94m" + " ▢ " + "\033[0m"
        else :
            if (valor == -1) :
                if (assist) :
                    linha += " 💣"
                else :
                    linha += "\033[94m" + " ▢ " + "\033[0m"
            else :
                if (valor > 8) :
                    if (valor == 9) :
                        linha += " ▢ "
                    else :
                        linha += " " + str (valor - 9) + " "
                else :
                    linha += "\033[94m" + " ▢ " + "\033[0m"
    return linha

def MarcarMatriz (pos, jogo, valor) :
    jogo [pos[0]][pos[1]] = valor

def verificar_resposta (tipo) :
    #0 = números, 1 = letras
    valido = False
    while valido == False :
        resposta = input ("Digite: ")
        respotaNumero = verificar_numero (resposta)
        if (tipo == 0 and respotaNumero == True) or (tipo == 1 and respotaNumero == False) :
            valido = True
        else :
            if (tipo == 0) :
                print ("Números apenas")
            else :
                print ("Letras apenas")
    return resposta

def Marcar_Pos (jogo, auto, num) :
    valido = False
    while (valido == False) :
        if (auto == True) :
            pos = [random.randint(0, len(jogo)+1), random.randint(0, len(jogo)+1)]
        else :
            pos = DigitarNumLetra ()
        if (-1 < pos [0] < len(jogo) and -1 < pos[1] < len(jogo)) :
            valor = jogo[pos[0]][pos[1]]
            if (valor < 9 and num != -1) or (valor != -1 and num == -1) :
            #if (num == -1 and valor != -1) or (num != -1) :
                valido = True
        else :
            if (auto == False) :
                print ("Digite um valor válido")
    if (num == -1) :
        jogo[pos[0]][pos[1]] = num
    return (pos)

def verificar_valor (matriz, pos, settingbombs, originalplay) :
    pontos = 0
    valorpos = matriz [pos[0]][pos[1]]
    soma = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
    tam = len (matriz)
    #atualizar valor pos incial
    if (valorpos != -1) :
        pontos += 1
        matriz [pos[0]][pos[1]] += 9
    else :
        if (settingbombs == False and originalplay == True) :
            print ("GameOver")
            pontos = -1  
    if (pontos != -1) :
        for i in range (8) :
            posver = [pos[0] + soma [i][0], pos [1] + soma [i][1]]
            if (-1 < posver[0] < tam and -1 < posver[1] < tam) :
                valor = matriz [posver[0]][posver[1]]
                if (valorpos == -1 and settingbombs == True) :
                    if (valor != -1) :
                        matriz [posver[0]][posver[1]] += 1
                else :
                    if (valor < 9) :
                        if (valorpos == 0) :  
                            if (valor == 0) :
                                pontos += verificar_valor (matriz, posver, False, False)
                            else :
                                pontos += 1
                                matriz [posver[0]][posver[1]] += 9
                                #ApresentarJogo (matriz, assist)
                                #time.sleep (0.02)
    else :
        pontos = -999
    return pontos

def PosicionarBombas (quantidade, matriz) :
    for i in range (quantidade) :
        verificar_valor (matriz, Marcar_Pos (matriz, True, -1), True, True)

def op_grid (numBomba) :
    print ("Selecione o novo tamanho do grid: 2 - 20")
    valido = False
    BombaNova = -1
    while (valido == False) :
        tamanho = verificar_resposta (0)
        if (1 < int(tamanho) < 21) :
            if (numBomba >= int(tamanho) * int(tamanho)) :
                BombaNova = int(tamanho)
            else :
                BombaNova = numBomba
            valido = True
        else :
            print ("Use um tamanho permitido.")
    return [int(tamanho), BombaNova]

def op_bombs (grid) :
    max = (grid * grid) - 1
    print ("Selecione o número de bombas: 1 - ", max)
    valido = False
    bombas = 0
    while (valido == False) :
        bombas = verificar_resposta (0)
        if (1 <= int(bombas) <= max) :
            valido = True
        else :
            print ("Use um número permitido.")
    return int(bombas)

def jogar (size, bombnumber, assist) :
    matriz = CriarMatriz (size)
    PosicionarBombas (bombnumber, matriz)
    meta = ((size * size) - bombnumber)
    pontos = 0
    ApresentarJogo (matriz, assist)
    fimDeJogo = False
    while (fimDeJogo == False) :
        pontos += verificar_valor (matriz, Marcar_Pos (matriz, False, 0), False, True)
        print ("\n\n\n")
        print (pontos)
        ApresentarJogo (matriz, assist)
        if (pontos >= meta or pontos < 0) :
            fimDeJogo = True
    if (pontos >= meta) :
        print ("Vitória")
    else :
        print ("Derrota")
    ApresentarJogo (matriz, True)
    input ("Aperte ENTER para sair")

def op_assist (assistorig) :
    assist = False
    if (assistorig == True) :
        assist = False
    else :
        assist = True
    return (assist)

#0 - vazio
#1 a 8 - Numero
#9 - vazio revelado
#10 a 17 - Numero revelado
#-1 - Bomba
#-3 - Nulo

assist = True
bombnumber = 8
size = 10





menu_id = 0
while menu_id == 0 :
    print ("   > [J]ogar <")
    print ("   > [O]pções <")
    resposta = verificar_resposta (1)
    menu_id = 0
    if (resposta.upper () == "O") :
        menu_id = 1
        while menu_id == 1 :
            print ("[G]rid atual: ", size,"x",size)
            assist_text = ""
            if (assist == True) :
                assist_text = "Ativado"
            else :
                assist_text = "Desativado"
            print ("[A]ssist Mode: " + assist_text)
            print ("[B]ombas: ", bombnumber)
            print ("[S]air")
            resposta = verificar_resposta (1)
            if (resposta.upper () == "G") :
                ops = op_grid (bombnumber)
                size = ops [0]
                print (ops [1])
                bombnumber = ops [1]
            else :
                if (resposta.upper () == "S") :
                    menu_id = 0
                else :
                    if (resposta.upper () == "A") :
                        assist = op_assist (assist)
                    else :
                        if (resposta.upper () == "B") :
                            bombnumber = op_bombs (size)
                        else :
                            print ("Use uma opção válida")
    else :
        if (resposta.upper () == "J") :
            jogar (size, bombnumber, assist)

