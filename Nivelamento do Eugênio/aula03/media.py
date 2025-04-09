soma = 0
for i in range(10):
    n = float(input('Digite a nota: '))
    soma += n
media = soma/10
print(f'A média das notas dos alunos foi {media:.1f}')