num = int(input('Digite um número: '))
n = str(num)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 


print(f'Seu número tem {u} unidades')
print(f'Seu número tem {d} dezenas')
print(f'Seu número tem {c} centenas')
print(f'Seu número tem {m} milhares')