# Macmult problemas com funções - 2
def encaixa(a, b):
    while b != 0 and a%10 == b%10:
# vê se o último digito do número é diferente de 0 e se os restos da divisão entre a e b por 10 são iguais
        a//= 10  # tira um digito de a
        b//= 10  # tira um digito de b
# efetua a divisão enquanto a condição acima for verdadeira
    return b == 0

# print(encaixa(123456, 3456))
# print(encaixa(567890, 890))

x = int(input('digite x: '))
y = int(input('digite y: '))

if x < y: # x sempre será o número maior
    aux = x
    x = y
    y = aux

maior = x
menor = y
segmento = False
while maior >= menor:
    if encaixa(maior, menor):
        segmento = True
    maior //= 10
if segmento:
    print(f'{y} é segmento de {x}')
else: 
    print(f'{y} não é segmento de {x}')