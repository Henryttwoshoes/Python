N = int(input())
contdentro = 0
contfora = 0
for i in range(10,N):
    if i >= 20 or i < 10:
        contfora += 1
    else:
        contdentro += 1
print(f'Há {contfora} valores fora do intervalo e {contdentro} dentro do intervalo.')