_author_ = 'Inkyy'

# Biblioteca
from random import sample
from colorama import Fore, Style
from time import sleep

# Grupos para o Sorteio;

grup1 = []
grup2 = []
grup3 = []
grup4 = []
grup5 = []
grup6 = []
grup7 = []
grup8 = []

# Lista para os números;

list_num = list(range(1,41))

# Loop para fazer 8 Sorteios;

for sort in range(8):

# Sorteio Dos grupos

    sort_num = sample(list_num, 5) # Para Usar o sample precisa de 2 condiçoes a primeira é o inicio e a 2 é o final, aqui eu usei a variaver list e para gerar 5 numeros.

# If para colocar cada sorteio em cada ranger escolhido;

    if sort == 0:
     grup1 = sort_num
    elif sort == 1:
        grup2 = sort_num
    elif sort == 2:
        grup3 = sort_num
    elif sort == 3:
        grup4 = sort_num
    elif sort == 4:
        grup5 = sort_num
    elif sort == 5:
        grup6 = sort_num
    elif sort == 6:
        grup7 = sort_num
    else:
        grup8 = sort_num

# Removendo os numeros da lista;

    for lista_remove in sort_num:
        list_num.remove(lista_remove)

# Codigo Bonito;

print('.'*80)
print(Fore.RED,Style.BRIGHT + 'ESTE PROGRAMA IRA FAZER SORTEIOS DOS GRUPOS DE TRABALHOS DE VOCÊS... BOA SORTE ☘️\033[m')
print('.'*80)
print(Fore.BLUE,Style.BRIGHT + '[O PROGRAMA IRA PEGAR O NUMERO DE CHAMADA COMO BASE, '
      'ENTÃO É SÓ VER O NÚMERO DE CHAMADA E VER O GRUPO QUE FOI SORTEADO.]\033[m 🦄')

print('\n')

print('.'*29)
print(Fore.GREEN,Style.BRIGHT + 'SORTEANDO OS GRUPOS.......\033[m ☘️')
print('.'*29)
print('\n')
sleep(2)

# Print Grupo 1;
print(Fore.YELLOW+'='*22)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 1 ❤️')
sleep(2)
print(Fore.CYAN, grup1)
print(Fore.YELLOW +'='*22)
print('\n')

# Print Grupo 2;
print(Fore.YELLOW +'='*22)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 2 ❤️❤️')
sleep(2)
print(Fore.CYAN, grup2)
print(Fore.YELLOW +'='*22)
print('\n')

# Print Grupo 3;
print(Fore.YELLOW +'='*22)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 3 ❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup3)
print(Fore.YELLOW +'='*22)
print('\n')

# Print Grupo 4;
print(Fore.YELLOW +'='*22)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 4 ❤️❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup4)
print(Fore.YELLOW +'='*22)
print('\n')

# Print Grupo 5;
print(Fore.YELLOW +'='*22)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 5 ❤️❤️❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup5)
print(Fore.YELLOW +'='*22)
print('\n')

# Print Grupo 6;
print(Fore.YELLOW +'='*25)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 6 ❤️❤️❤️❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup6)
print(Fore.YELLOW+'='*25)
print('\n')

# Print Grupo 7;
print(Fore.YELLOW +'='*26)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 7 ❤️❤️❤️❤️❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup7)
print(Fore.YELLOW +'='*26)
print('\n')

# Print Grupo 8;
print(Fore.YELLOW+'='*28)
print(Fore.LIGHTMAGENTA_EX,Style.BRIGHT + 'GRUPO 8 ❤️❤️❤️❤️❤️❤️❤️❤️')
sleep(2)
print(Fore.CYAN, grup8)
print(Fore. YELLOW+'='*28)
print('\n')
print('FIM 😊\n\n'
      'OBRIDADO 🥰')