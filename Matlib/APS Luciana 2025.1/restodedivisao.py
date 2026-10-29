escolha = 'S'


while escolha == 'S':
    numero = int(input('Digite o número: '))
    print(f'o resto da divisão dá {numero % 16} e quociente {numero // 16}')
    decisão = input('Deseja calcular de novo? ')
    escolha = decisão

