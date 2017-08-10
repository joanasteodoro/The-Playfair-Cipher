#Tipos abstratos de dados

#Tipo posicao
#Construtores
def faz_pos (l,c):
    #Funcao que cria um tuplo com o valor da linha e coluna de um elemento da chave, respetivamente
    #Verifica, ainda, se os argumentos introduzidos sao inteiros
    if not isinstance (l, int) or not isinstance (c, int) or l < 0 or c < 0:
        raise ValueError('faz_pos: argumentos errados')
    else:
        return (l,c)
    
#Seletores
#Funcoes que devolvem o numero da linha/coluna da posicao colocada no argumento p
def linha_pos (p):
    return p[0]
def coluna_pos (p):
    return p[1]

#Reconhecedores
#Verificam se o argumento e um tuplo de tamanho dois com numeros inteiros
def e_pos (arg):
    return isinstance (arg, tuple) and len (arg) == 2 and isinstance (arg[0], int) and isinstance (arg[1], int) and arg[0] > 0 and arg[1] > 0
    
#Testes
#Verificam se duas posicoes sao exatamente as mesmas (igual linha e coluna)
def pos_iguais (p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

#Tipo chave
#Construtores
def gera_chave_aux (l, mgc):
    #Funcao auxiliar que, a partir da mensagem de geracao de chave, retira todos os espacos e letras repetidas desta
    chave = mgc.replace (' ', '')
    chave_final = []
    for letra in chave:
        if letra not in chave_final:
            chave_final += [letra]
    for letra in l:
        if letra not in chave_final:
            chave_final += [letra]
    return chave_final

def verifica_maiusculas(l):
    #Funcao auxiliar que verifica se todos os elementos do tuplo sao maiusculas
    tuplo = ()
    for c in l:
        if c != c.lower():
            tuplo += (c, )
    return len(tuplo)

def verifica_mgc(mgc):
    #Funcao auxiliar que verifica se todos os elementos da mensagem de geracao de chave sao maiusculas
    tuplo = ()
    for c in mgc:
        if c == c.upper():
            tuplo += (c, )
    return len(tuplo)

def verifica_els_diferentes (l):
    #Funcao auxiliar que verifica se todos os elementos do tuplo sao diferentes
    tuplo = ()
    for c in l:
        if c not in tuplo:
            tuplo += (c, )
    return len(tuplo)

def gera_chave_linhas (l, mgc):   
#Funcao que gera a chave disposta por linhas     
    if not isinstance(l, tuple) or len(l) != 25 or len(mgc) != verifica_mgc(mgc) or 25 != verifica_els_diferentes(l):
        raise ValueError('gera_chave_linhas: argumentos errados')
    mens = gera_chave_aux(l, mgc)    
#Gerar tabela disposta por 5 linhas, que se apresenta numa lista
    tabela = []
    linha, inicio, fim = 0, 0, 5
    while linha**2 != 25:
        linha += 1
        tabela += [mens[inicio:fim]]
        inicio, fim = fim, fim + 5
    return tabela   
    
def gera_chave_espiral (l, mgc, s, pos):
    #Funcao que gera a chave numa tabela 5x5 em espiral de acordo com o sentido (s) e a posicao (pos) introduzidos
    if not isinstance(l, tuple) or len(l) != 25 or not isinstance(s, str) or not isinstance(pos, tuple) or len(mgc) != verifica_mgc(mgc) or verifica_maiusculas(l) != 25 or 25 != verifica_els_diferentes(l):
        raise ValueError('gera_chave_espiral: argumentos errados')        
    mens = gera_chave_aux (l, mgc) #a funcao auxiliar e chamada para obter as letras finais
    baixo, cima, esq, drt = (1, 0), (-1, 0), (0, -1), (0, 1) #tuplos que representam o incremento/decremento da linha/coluna
    #dicionarios que demonstram o sentido da criacao da chave em espiral de acordo com a posicao
    seg = {(0, 0): (drt, baixo), (0,4): (baixo, esq), (4, 4):(esq, cima), (4, 0): (cima, drt)}
    dic_direcao = {drt: (baixo, cima), baixo: (esq, drt), esq: (cima, baixo), cima: (drt, esq)}
    matriz = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    if s == 'r':
        ind = 0 #ind representa o indice de dic_direcao usado para obter o sentido da espiral
    elif s == 'c':
        ind = 1
    sentido = seg[pos][ind] #sentido que a matriz tera a partir de s
    i, j = pos[0], pos[1]
    for letra in mens: #ciclo que permite preencher a matriz 
        if i >= 0 and i <= 4 and j >= 0 and j <= 4 and matriz[i][j] == '':
            matriz[i][j] = letra
        else:
            #e necessario decrementar os indices i e j, uma vez que percorrem o sentido ate uma posicao invalida ou uma que ja se encontra preenchida
            i -= sentido[0]
            j -= sentido[1]
            #quando se decrementa os indices significa que ja chegamos ao fim de uma linha ou coluna, logo o sentido altera-se
            sentido = dic_direcao[sentido][ind] 
            i += sentido[0]
            j += sentido[1]
            matriz[i][j] = letra
        i += sentido[0]
        j += sentido[1]
    return matriz

#Seletor
#Selecionam um elemento de chave a partir desta e de uma posicao
def ref_chave (c, p):
    return c[p[0]][p[1]]

#Modificador
#Modificam uma letra da chave quando dada a propria chave, uma posicao e a letra que se pretem ter
def muda_chave (c, p, l):
    c[p[0]][p[1]] = l
    return c

#Reconhecedores
#verificam se a chave e uma lista de 5 listas em que cada uma tem 5 elementos do tipo string em letra maiscula
def e_chave(arg):
    def verifica_comp_linhas (arg):
        a = 0
        for i in range(5):
            if len(arg[i]) == 5:
                a += 5
        return a
    def verifica_elementos (arg):
        for linha in arg:
            for i in range(5):
                if not isinstance(linha[i], str) or linha[i] == linha[i].lower():
                    return False
        return True
    return isinstance (arg, list) and len(arg) == 5 and verifica_comp_linhas(arg) == 25 and verifica_elementos(arg)

#Transformadores
#Imprime a tabela 5x5 da chave
def string_chave (c):
    tabela_aux = ''
    tabela = ''
    for linha in c:
        for letra in linha:
            tabela_aux += letra + ' '  
    for car in range(len(tabela_aux)):
        if (car + 1) % 10 == 0:
            tabela += tabela_aux[car] + '\n'
        else:
            tabela += tabela_aux[car]
    return tabela

def digramas (mens):
    #Funcao que cria os digramas da mensagem introduzida
    mens = mens.replace (' ', '') #retiram-se os espacos da mensagem
    digrm = ''    
    while len(mens) >= 2: #verificam-se todos os casos, de duas em duas letras (quando a mensagem tem um numero de caracteres par, basta entrar neste ciclo para obter os digramas finais)
        if mens[0] == mens[1]:
            digrm += mens[0] + 'X'
            mens = mens[1:]
        else:
            digrm += mens[0] + mens[1]
            mens = mens[2:]
    #quando o numero de caracteres da mensagem e impar, e preciso adicionar, aos digramas finais, a ultima letra, assim como 'X'
    if len(mens) == 1:
        digrm += mens + 'X'
    return digrm

def figura (digrm, chave):
    #Funcao que devolve a figura obtida pelo digrama introduzido, assim como as posicoes das letras deste
    for linha in range(5):
        for letra in range(5):
            if digrm[0] == chave[linha][letra]:
                pos1 = (linha, letra)
            elif digrm[1] == chave[linha][letra]:
                pos2 = (linha, letra)
    if pos1[0] == pos2[0]:
        return ('l', pos1, pos2)
    elif pos1[1] == pos2[1]:
        return ('c', pos1, pos2)
    else:
        return ('r', pos1, pos2)
    
def codifica_l (pos1, pos2, inc):
    #Funcao que encripta ou desencripta as posicoes das letras numa linha dadas pelo utilizador a partir do argumento inc
    pos1_cod, pos2_cod = (pos1[0], ), (pos2[0], )
    if inc == 1: #encriptacao
        if pos1[1] == 4:
            pos1_cod += (0, )
        else:
            pos1_cod += (pos1[1] + 1, )
        if pos2[1] == 4:
            pos2_cod += (0, )
        else:
            pos2_cod += (pos2[1] + 1, )
    elif inc == -1: #desencriptacao
        if pos1[1] == 0:
            pos1_cod += (4, )
        else:
            pos1_cod += (pos1[1] - 1, )
        if pos2[1] == 0:
            pos2_cod += (4, )
        else:
            pos2_cod += (pos2[1] - 1, )            
    return (pos1_cod, pos2_cod)

def codifica_c (pos1, pos2, inc):
    #Funcao que encripta ou desencripta as posicoes das letras numa coluna dadas pelo utilizador a partir do argumento inc
    pos1_cod, pos2_cod = list(pos1), list(pos2)
    if inc == 1: #encriptacao
        if pos1[0] == 4:
            pos1_cod[0] = 0
        else:
            pos1_cod[0] = pos1[0] + 1
        if pos2[0] == 4:
            pos2_cod[0] = 0
        else:
            pos2_cod[0] = pos2[0] + 1
    elif inc == -1: #desencriptacao
        if pos1[0] == 0:
            pos1_cod[0] = 4
        else:
            pos1_cod[0] = pos1[0] - 1
        if pos2[0] == 0:
            pos2_cod [0] = 4
        else:
            pos2_cod[0] = pos2[0] - 1  
    pos1_cod, pos2_cod = tuple(pos1_cod), tuple(pos2_cod)
    return (pos1_cod, pos2_cod)

def codifica_r (pos1, pos2):
    #Funcao que encripta ou desencripta as posicoes das letras que formam um retangulo
    pos1_cod = (pos1[0], pos2[1])
    pos2_cod = (pos2[0], pos1[1])
    return (pos1_cod, pos2_cod)

def codifica_digrama (digrm, chave, inc): 
    #Funcao que retorna o digrama encriptado ou desencriptado (de acordo com inc)
    fig = figura (digrm, chave) #obtem a figura formada pelas letras para facilitar a obtencao do resultado
    if fig[0] == 'r':
        posicoes_cod = codifica_r (fig[1], fig[2])
    elif fig[0] == 'l':
        posicoes_cod = codifica_l (fig[1], fig[2], inc)
    else:
        posicoes_cod = codifica_c (fig[1], fig[2], inc)
    #usa-se o seletor para selecionar a letra que se pretende na chave
    letra_1 = ref_chave(chave,(posicoes_cod[0][0],posicoes_cod[0][1]))
    letra_2 = ref_chave(chave, (posicoes_cod[1][0], posicoes_cod[1][1]))
    return letra_1 + letra_2

def codifica (mens, chave, inc):
    #funcao que codifica a mensagem
    mensagem = digramas(mens) #transforma-se a mensagem em digramas
    mensagem_final = ''
    while len(mensagem) > 0:
        #codifica-se digrama a digrama e retiram-se os digramas ja codificados da mensagem
        mensagem_final += codifica_digrama(mensagem[0:2], chave, inc)   
        mensagem = mensagem[2:]
    return mensagem_final