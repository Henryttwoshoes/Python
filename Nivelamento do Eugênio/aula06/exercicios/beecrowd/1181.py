L = int(input())
T = input().strip().upper()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

linha_escolhida = matriz[L]

if T == 'S':
    resultado = sum(linha_escolhida)
if T == 'M':
    resultado = sum(linha_escolhida)/12

print(f'{resultado:.1f}')                
    