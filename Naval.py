#Felipe Peixoto de Oliveira - Engenharia de Software

from copy import deepcopy
import random
from typing import SupportsBytes

def CriarMatriz (largura) :
    matriz = []
    for i in range (largura) :
        linha = []
        for i in range (largura) :
            linha.append (0)
        matriz.append (linha)
    return matriz

def RetornarAlfabeto () :
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def CriarLinha (matriz, i, hide, assist) :
    linha = ""
    for j in range (len (matriz)) :
        valor = matriz [i][j]
        if (valor == 0) :
            linha += "\033[94m" + "~~~" + "\033[0m"
        else :
            if (valor == -1) :
                linha += "\033[91m" + " X " + "\033[0m"
            else :
                if (valor < 5) :
                        if (hide == True) :
                            if (assist) :
                                linha += "~~~"
                            else :
                                linha += "\033[94m" + "~~~" + "\033[0m"
                        else :
                            graficos = ["", "S", "C", "T", "P"]
                            ind = int (valor)
                            graph = graficos [ind]
                            linha += " " + graph + " "
                else :
                    if (valor == 5) :
                        linha += " " + "\033[91m" + "✸" + "\033[0m" + " "
                    else :
                        linha += "\033[1m" + "~" + "o" + "~" + "\033[0m"
    return linha

def ApresentarJogo (matriz, matriz2, assist) :
    nums = "  "
    for j in range (len (matriz)) :
        if (j > 9) :
            nums += " " + str(j + 1)
        else :
            nums += " " + str(j + 1) + " "
    if (matriz2 == None) :
        print (nums)
    else :
        print (nums + "   " + nums)
    for i in range (len (matriz)) :
        linha = ""
        alfabeto = RetornarAlfabeto ()
        
        linha1 = CriarLinha (matriz, i, False, False)
        if (matriz2 == None) :
            linha2 = ""
        else :
            linha2 = CriarLinha (matriz2, i, True, assist) + " " + alfabeto [i]
        linha += alfabeto [i] + " " + linha1 + "      " + linha2
        print (linha)

def verificar_numero (valor) :
    resultado = True
    try:
        valor = int(valor)
    except ValueError:
        resultado = False
    return resultado

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

def DesenharBarco (barco, rot) :
    barcolista = ["Submarino", "Contratropeiro", "Navio-Tanque", "Porta-Avião"]
    barcografico = ""
    graficofinal = ""
    if (rot == True) :
        graficofinal = "\n"
    else :
        graficofinal = " "
    for i in range (barco) :
        barcografico += "o" + graficofinal
    print (barcografico)
    print (barcolista [barco - 1])

def PrepararGrid (frota, jogo, auto) :
    for i in range (len (frota)) :
        MarcarMatriz (EscolherPos (jogo, frota [i], auto), jogo, frota [i], auto)

def DigitarNumLetra () :
    coluna = 0
    linha = 0
    print ("Digite uma letra: ")
    linha = ValorIgualLista (verificar_resposta (1).upper (), RetornarAlfabeto ())
    print ("Digite um número: ")
    coluna = int (verificar_resposta (0)) - 1
    return [linha, coluna]

def EscolherPos (jogo, barco, auto) :
    if (auto == False) :
        DesenharBarco (barco, False)
    rota = 0
    if (auto == False) :
        print ("[H]orizontal ou [V]ertical")
        rot = verificar_resposta (1)
        if (rot == "h") :
            rota = 1
            DesenharBarco (barco, False)
        else :
            rota = 0
            DesenharBarco (barco, True)
    else :
        rota = random.randint(0, 2)
    valido = False
    while (valido == False) :
        if (auto == False) :
            posO = DigitarNumLetra ()
        else :
            posO = [random.randint(0, len(jogo)+1), random.randint(0, len(jogo)+1)]
            rota = rota
        pos = [posO[0], posO[1], rota]
    #verificar pos
        acertos = 0
        jogoteste = deepcopy (jogo)
        for i in range (barco) :
            posteste = 0
            try :
                if (rota == 0) :
                    posteste = jogo [pos[0] + i][pos[1]]
                else :
                    posteste = jogo [pos[0]][pos[1] + i]
            except :
                posteste = -1
            else :
                if (posteste == 0) :
                    posteste = barco
                    acertos += 1
                else :
                    posteste = -1
                if (rota == 0) :
                    jogoteste [pos[0] + i][pos[1]] = posteste
                else :
                    jogoteste [pos[0]][pos[1] + i] = posteste
        if (acertos == barco) :
            valido = True
        else :
            if (auto == False) :
                ApresentarJogo (jogoteste, None, False)
                print ("Posição inválida")
    return pos

def MarcarMatriz (pos, jogo, barco, auto) :
    for i in range (barco) :
        if (pos [2] == 0) :
            jogo [pos[0] + i][pos[1]] = barco
        else :
            jogo [pos[0]][pos[1] + i] = barco
    if (auto == False) :
        ApresentarJogo (jogo, None, False)
    
def Atacar (jogo, auto, vida) :
    valido = False
    while (valido == False) :
        if (auto) :
            pos = [random.randint(0, len(jogo)+1), random.randint(0, len(jogo)+1)]
        else :
            pos = DigitarNumLetra ()
        if (-1 < pos [0] < len(jogo) and -1 < pos[1] < len(jogo)) :
            valor = jogo[pos[0]][pos[1]]
            if (valor != 5 and valor != 6 and valor != 7) :
                valido = True
        else :
            print ("Digite um valor válido")
    if (valor != 0) :
        jogo[pos[0]][pos[1]] = 5
        print ("Acertou")
        vida -= 1
    else :
        jogo[pos[0]][pos[1]] = 6
    return vida

def verificar_numero (valor) :
    resultado = True
    try:
        valor = int(valor)
    except ValueError:
        resultado = False
    return resultado

#numero = 0, letra = 1
def verificar_resposta (tipo) :
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


def op_grid () :
    print ("Selecione o novo tamanho do grid: 7 - 17")
    valido = False
    while (valido == False) :
        tamanho = verificar_resposta (0)
        if (verificar_numero (tamanho) and 6 < int(tamanho) < 18) :
            valido = True
        else :
            print ("Use um tamanho permitido")
    return tamanho

def op_assist () :
    print ("       [ Com o Assist Mode, a posição dos barcos do adversário será revelada ]")
    print ("Digite [A] para ativar o Assist Mode, digite qualquer outra letra para desativar.")
    op = verificar_resposta (1)
    assist = False
    if (op.upper () == "A") :
        assist = True
    else :
        assist = False
    return (assist)

def DesenharFrota (frota) :
    #sub-contra-navio-porta
    f = [0, 0, 0, 0]
    for i in range(len(frota)) :
        n = frota [i]
        f [n - 1] += 1
    frase = "[ " + str(f[0]) + "x Submarino - " + str(f[1]) + "x Contratropeiro - " + str(f[2]) + "x Navio - " + str(f[3]) + "x Porta-Avião ]"
    return (frase)


def EscolherFrota () :
    print ("Escolha uma das opções pré-existentes ou crie uma frota [C]ustomizada.")
    print ("[T]radicional - 4 Submarinos, 3 Contratropeiros, 2 Navio-Tanques, 1 Porta-Avião")
    print ("[R]everso - 3 Porta-Aviões, 2 Navio-Tanques, 1 Contratropeiro, 1 Submarino")
    print ("[P]alheiro - 4 porta-aviões, 1 submarino")
    print ("[S]udden Death - 1 Submarino")
    op = verificar_resposta (1).upper ()
    frota = []
    if (op == "C") :
        finalizar = False
        frotaCustom = []
        Adicionar = True
        while (finalizar == False) :
            navioSelecionado = 0
            print (DesenharFrota (frotaCustom))
            print ("[S]ubmarino (1) - [C]ontratropeiro (2) - [N]avio-Tanque (3) - [P]orta-Avião (4) - [F]inalizar")
            if (Adicionar) :
                print ("Digite um navio para adicionar, caso queira remover, digite [R]")
            else :
                print ("Digite um navio para remover, caso queira adicionar, digite [R]")
            nav = verificar_resposta (1).upper ()
            if (nav == "S") :
                navioSelecionado = 1
            else :
                if (nav == "C") :
                    navioSelecionado = 2
                else :
                    if (nav == "N") :
                        navioSelecionado = 3
                    else :
                        if (nav == "P") :
                            navioSelecionado = 4
                        else :
                            if (nav == "R") :
                                navioSelecionado = 5
                            else :
                                if (nav == "F") :
                                    navioSelecionado = 6
            if (navioSelecionado > 0 and navioSelecionado < 5) :
                if (Adicionar) : 
                    frotaCustom.append (navioSelecionado)
                else :
                    try :
                        frotaCustom.remove (navioSelecionado)
                    except :
                        print ("Não existe esse navio na frota")
            else :
                if (navioSelecionado == 5) :
                    if (Adicionar) :
                        print ("Agora você está removendo navios")
                        Adicionar = False
                    else :
                        print ("Agora você está adicionando navios")
                        Adicionar = True
                else :
                    if (navioSelecionado == 6) :
                        print ("Frota finalizada")
                        frota = frotaCustom
                        finalizar = True
                    else :
                        print ("Selecione uma opção válida")   
    else :
        if (op == "T") :
            frota = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        else :
            if (op == "R") :
                frota = [4, 4, 4, 3, 3, 2, 1]
            else :
                if (op == "P") :
                    frota = [4 ,4 , 4 ,4 , 1]
                else :
                    if (op == "S") :
                        frota = [1]
                    else :
                        print ("Use uma opção válida")
    return (frota)

def jogar (tamanho, assist, frota) :
    jogo1 = CriarMatriz (int(tamanho))
    jogo2 = CriarMatriz (int(tamanho))
    ApresentarJogo (jogo1, jogo2, assist)
    vida = 0
    for i in range (len (frota)) :
        vida += frota [i]
    jogo1vida = vida
    jogo2vida = vida
    print (" Digite [A] para organizar sua frota automaticamente, digite qualquer outra letra para prosseguir tradicionalmente")
    op = verificar_resposta (1)
    organizar_random = False
    if (op.upper() == "A") :
        organizar_random = True
    PrepararGrid (frota, jogo1, organizar_random)
    PrepararGrid (frota, jogo2, True)
    #PrepararGrid ([2, 2, 3, 4], jogo2, True)
    vitoria = False
    while (vitoria == False) :
        print ("\n\n\n")
        ApresentarJogo (jogo1, jogo2, assist)
        jogo2vida = Atacar (jogo2, False, jogo2vida)
        jogo1vida = Atacar (jogo1, True, jogo1vida)
        if (jogo2vida == 0 or jogo1vida == 0) :
            print ("")
            print ("============================")
            print ("")
            if (jogo2vida == 0) :
                print ("Vitória do jogador!")
            else :
                print ("Vitória do computador!")
            input ("Aperte qualquer tecla para voltar para a tela inicial") 
            vitoria = True




# Grid Layout
# 0 - vazio
# 1 - Submarino s - 7
# 2 = contratropeiro c - 8  
# 3 = navio tanque t - 9
# 4 - porta avião p - 10
# 5 - Acerto
# 6 - erro

#menu = 0
#opções = 1
tamanho = 10
menu_id = 0
assist = False
frota = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
#menu
while menu_id == 0 :
    print ("   > [J]ogar <")
    print ("   > [O]pções <")
    resposta = verificar_resposta (1)
    menu_id = 0
    if (resposta.upper () == "O") :
        menu_id = 1
        while menu_id == 1 :
            print ("[G]rid atual: ", tamanho)
            assist_text = ""
            if (assist == True) :
                assist_text = "Ativado"
            else :
                assist_text = "Desativado"
            print ("[A]ssist Mode: " + assist_text)
            print ("[F]rota: ", DesenharFrota (frota))
            print ("[S]air")
            resposta = verificar_resposta (1)
            if (resposta.upper () == "G") :
                tamanho = op_grid ()
            else :
                if (resposta.upper () == "S") :
                    menu_id = 0
                else :
                    if (resposta.upper () == "A") :
                        assist = op_assist ()
                    else :
                        if (resposta.upper () == "F") :
                            frota = EscolherFrota ()
                        else :
                            print ("Use uma opção válida")
    else :
        if (resposta.upper () == "J") :
            jogar (tamanho, assist, frota)