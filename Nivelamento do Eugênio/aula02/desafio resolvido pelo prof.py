codigo, quantidade, preco = input().split()
codigo = int(codigo)
quantidade = int(quantidade)
preco = float(preco)

codigo1, quantidade1, preco1 = input().split()
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
preco1 = float(preco1)

valor = quantidade * preco + quantidade1 * preco1
print(f'VALOR A PAGAR: R$ {valor:.2f}') # saída