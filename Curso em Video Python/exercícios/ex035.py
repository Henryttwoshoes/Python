print('-='*20)
print('ANALISADOR DE TRIÂNGULOS!')
print('-='*20)
s1 = float(input('Digite o 1o segmento: '))
s2 = float(input('Digite o 2o segmento: '))
s3 = float(input('Digite o 3o segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo! :D')
else:
    print('Os segmentos acima não podem formar um triângulo :(')