import random

def imprime_mensagem_abertura ():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

def escolhe_palavra_inicial():
    palavras_secretas = []
    with open("palavras.txt", "r") as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip()
            palavras_secretas.append(palavra)
    aleatoria = random.randrange(0, len(palavras_secretas))
    return palavras_secretas[aleatoria].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def verifica_letra_chutada(chute,palavra_secreta,letras_acertadas):
    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (letra.upper() == chute.upper()):
                letras_acertadas[index] = letra
            index += 1

def logica_da_forca(palavra_secreta):
    enforcou = False
    acertou = False
    erros = 0
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    while (not enforcou and not acertou):
        chute = input('Digite uma letra que será seu chute:').strip().upper()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra.upper() == chute.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == len(palavra_secreta) - 4
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)
    if (acertou):
        print("Parabéns você acertou a palavra")
    else:
        print("Fim do jogo você enforcou!")

def marca_letra_acertada(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letras_acertadas[index] = letra
        index += 1

def verifica_se_enforcou(erros, letras_acertadas, palavra_secreta):
    enforcou = erros == len(palavra_secreta) - 4
    acertou = '_' not in letras_acertadas
    return acertou, enforcou

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = escolhe_palavra_inicial()
    enforcou = False
    acertou = False
    erros = 0
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    while (not enforcou and not acertou):
        chute = input('Digite uma letra que será seu chute:').strip().upper()
        if (chute in palavra_secreta):
            marca_letra_acertada(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
        acertou, enforcou = verifica_se_enforcou(erros, letras_acertadas, palavra_secreta)
        print(letras_acertadas)
    if (acertou):
        print("Parabéns você acertou a palavra")
    else:
        print("Fim do jogo você enforcou!")

if (__name__ == '__main__'):
    jogar()
