# Função que conta quantas vezes um dígito 'd' aparece no número 'n'
def contadigitos(n, d):
    q = n  # Copia o valor de 'n' para 'q' para manipulação
    cont = 0  # Inicializa o contador de ocorrências do dígito
    while q > 0:  # Enquanto ainda houver dígitos em 'q'
        digito = q % 10  # Obtém o último dígito de 'q'
        if digito == d:  # Verifica se o dígito é igual a 'd'
            cont += 1  # Incrementa o contador se for igual
        q //= 10  # Remove o último dígito de 'q' (divisão inteira por 10)
    return cont  # Retorna o número de ocorrências de 'd' em 'n'

# Testes da função contadigitos
print('-----------contadigitos---------')
print(contadigitos(111111, 1))  # Conta quantas vezes o dígito 1 aparece em 111111
print(contadigitos(111111, 3))  # Conta quantas vezes o dígito 3 aparece em 111111
print(contadigitos(123456789, 9))  # Conta quantas vezes o dígito 9 aparece em 123456789
print('--------------------------------')

# Entrada de dois números inteiros para verificar se são permutações
x = int(input('digite x: '))  # Lê o primeiro número
y = int(input('digite y: '))  # Lê o segundo número

# Inicializa a variável que indica se os números são permutações
permutaçao = True

# Verifica se os dois números têm a mesma quantidade de cada dígito de 1 a 9
for d in range(1, 10):  # Itera pelos dígitos de 1 a 9
    if contadigitos(x, d) != contadigitos(y, d):  # Compara a quantidade de cada dígito
        permutaçao = False  # Se a quantidade for diferente, não são permutações
        break  # Interrompe o loop, pois já sabemos que não são permutações

# Exibe o resultado
if permutaçao:
    print(f'{x} é permutação de {y}')  # Se 'permutaçao' for True, os números são permutações
else:
    print(f'{x} não é permutação de {y}')  # Caso contrário, não são permutações