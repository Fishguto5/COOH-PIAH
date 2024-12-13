import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

          
######################################################################################
def soma_caracteres(texto):
    '''calcula a soma de todos os caracteres do texto'''
    '''soma das letras de todas as palavras'''
    funcao=quantidade_palavras(texto)
    contagem=len(funcao)
    alteravel=0
    soma=0
    while contagem>alteravel:
        tamanho_novo=len(funcao[alteravel])
        soma=soma+tamanho_novo
        alteravel+=1
    return soma
####################################################################################
def quantidade_palavras(texto):
    '''retorna a lista de palavras do texto'''
    funcao=quantidade_frases(texto)
    comprimento=len(funcao)
    lista_palavra=[]
    mudante=0
    while comprimento>mudante:
        for tamanho_palavra in separa_palavras(quantidade_frases(texto)[mudante]):
            lista_palavra.append(tamanho_palavra)
        mudante+=1
    palavras= lista_palavra

    return palavras
###################################################################################
def quantidade_frases(texto):
    '''retorna a lista de frases do texto'''
    funcao=quantidade_sentença(texto)
    tamanho=len(funcao)
    variavel=0
    lista_frase=[]
    while tamanho>variavel:
        for frase in separa_frases(funcao[variavel]):
            lista_frase.append(frase)
            frases=lista_frase
        variavel+=1

    return frases
#################################################################################
def quantidade_sentença(texto):
    '''retorna a lista de sentença do texto'''
    lista_sentencas=[]
    for i in separa_sentencas(texto):
        lista_sentencas.append(i)
    sentenca=lista_sentencas

    return sentenca
################################################################################    
def tamanho_medio(texto):
    '''calcula o ''tamanho médio'' do texto'''
    funcao=quantidade_frases(texto)
    comprimento=len(funcao)
    soma=soma_caracteres(texto)
    lista_palavra=[]
    mudante=0
    while comprimento>mudante:
        for tamanho_palavra in separa_palavras(funcao[mudante]):
            lista_palavra.append(tamanho_palavra)
        mudante+=1
    tamanho_medio=soma/len(lista_palavra)
    
    return tamanho_medio
################################################################################
def Hapax_Legomana(texto):
    '''calcula a relação Hapax Legomana'''
    denominador=len(quantidade_palavras(texto))
    palavras_unicas=n_palavras_unicas(quantidade_palavras(texto))
    Hapax_Legomana= palavras_unicas/denominador

    return Hapax_Legomana
###############################################################################
def Type_Token(texto):
    '''calcula a razão Type Token'''
    denominador=len(quantidade_palavras(texto))
    palavras_diferentes=n_palavras_diferentes(quantidade_palavras(texto))
    Type_token=palavras_diferentes/denominador
    return Type_token
################################################################################
def Tamanho_medio_de_sentenca(texto):
    '''calcula o tamanho médio das sentaças do texto'''
    denominador=len(quantidade_sentença(texto))
    inicio=0
    soma=0
    for caracteres in range(denominador):
        tamanho=len(quantidade_sentença(texto)[caracteres])
        inicio+=1
        soma=soma+tamanho
    tamanho_medio_sentenca= soma/denominador
    
    return tamanho_medio_sentenca
#################################################################################
def Complexidade_de_sentença(texto):
    qte_frases=len(quantidade_frases(texto))
    qte_sentenca=len(quantidade_sentença(texto))
    complexidade=qte_frases/ qte_sentenca

    return complexidade
#################################################################################
def Tamanho_medio_frase(texto):
    inicio=0
    soma=0
    qte_frases=len(quantidade_frases(texto))
    for caracter in range (qte_frases):
        tamanho=len(quantidade_frases(texto)[inicio])
        inicio+=1
        soma=soma+tamanho
    tamanho_medio=soma/qte_frases
    
    return tamanho_medio
        
###########################################################################        
def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    '''as_a e as_b são listas com os traços linguísticos da assinatura - como tamanho médio, Type Token etc'''
    lista_diferenca=[]
    i=0
    while i<=5: 
        diferenca=as_a[i]-as_b[i]
        if diferenca<0:
            diferenca=diferenca*(-1)
            lista_diferenca.append(diferenca)
        else:
            lista_diferenca.append(diferenca)
        i+=1
    soma=0
    for valor in lista_diferenca:
        soma+=valor
    return abs(soma/6)
        
#####################################################################################    
def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = float(tamanho_medio(texto))
    ttr = float(Type_Token(texto))
    hlr = float(Hapax_Legomana(texto))
    sal = float(Tamanho_medio_de_sentenca(texto))
    sac = float(Complexidade_de_sentença(texto))
    pal = float(Tamanho_medio_frase(texto))

    return [wal, ttr, hlr, sal, sac, pal]

############################################################################
def avalia_textos(textos,ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_ass=[]
    for texto in textos:
        ass=calcula_assinatura(texto)
        lista_ass.append(ass)
    lista_grau=[]
    for sla in lista_ass:
        grau=compara_assinatura(sla,ass_cp)
        lista_grau.append(grau)
    tamanho=len(textos)
    j=0
    indice=1
    indice_texto=1
    numero=1
    mudar=True
    menor=lista_grau[0]
    lista_indice=[]
    if tamanho>1: 
        for valor in range (tamanho-1):
            if lista_grau[j]>lista_grau[j+1]:
                compara = lista_grau[j+1]
                guarda=compara
                if menor>guarda:
                    menor = guarda
                    numero=indice
                    indice_final=numero+1
            else:
                numero=indice
                valor_fixo=numero
                lista_indice.append(numero)
                indice_final=lista_indice[0]
            if lista_grau[j]==lista_grau[j+1]:
                indice_final=1
            j+=1
            indice+=1
    if tamanho == 1:
        indice_final=1

    return indice_final
###################################################################################
'''CÓDIGO COMEÇA A RODAR AQUI S2'''
def main():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    ass_cp=le_assinatura()
    textos=le_textos()
    avalia=avalia_textos(textos,ass_cp)
    print()
    print("O autor do texto",avalia,"está infectado com COH-PIAH")

main()






    
    

    

    
    
        

   
    
    

    
    
