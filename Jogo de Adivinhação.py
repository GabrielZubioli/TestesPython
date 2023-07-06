import random
import os
dica2 = ""
Erro = 1
def limpa():
    if os.name == 'nt':
        _=os.system('cls')

def sortear (inicio, fim):
    num_sorteado = random.randint (inicio, fim)
    return num_sorteado
nivel = int(input("Qual nivel você deseja jogar?\n" "Facil   (Digite 1)\n" "Medio   (Digite 2)\n" "Dificil (Digite 3)\n"))

if nivel == 1:
    inicio = 1
    fim = 10
elif nivel == 2:
    inicio = 1
    fim = 50
else :
    inicio = 1
    fim = 100
num_aleatorio = sortear (inicio,fim)

if num_aleatorio % 2 == 0:
    dica = "O numero é par"
else :
    dica = "O numero é impar"
tentativa = int(input("\nTente adivinhar o numero de 1 a {}:".format(fim)))

while tentativa != num_aleatorio:
    limpa ()
    print (dica,dica2, "/ Tentativas :", Erro)
    tentativa = int(input("Você errou, tente adivinhar outro numero: "))
    Erro = Erro + 1

    if num_aleatorio > tentativa:
        dica2 = "/ O Numero é maior que a resposta anterior"
    else :
        dica2 = "/ O Numero é menor que a resposta anterior"
    if Erro == 10:
        tentativa = num_aleatorio
        final = "Você Perdeu!"
    else:
        final = "Parabens, Você acertou!"
pontuacao = 10 - Erro
limpa()
print(final,"\nO numero era", num_aleatorio, "\nVocê marcou {} pontos".format(pontuacao))