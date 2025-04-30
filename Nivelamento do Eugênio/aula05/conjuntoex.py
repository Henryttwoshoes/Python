'''

Conjunto - valores entre chaves sem ordem {}


'''

conjunto = {1, 2, 'três', 'quatro', 5}
conjunto3 = {1,5,7}


print(len(conjunto))

print( 1 in conjunto)
print( 0.5 in conjunto)

conjunto2 = conjunto | {6} # união

print(conjunto2)

print(conjunto & conjunto2)

print(conjunto - conjunto3) # subtração dos conjuntos
'''
A subtração pega todos os elementos iguais dos dois conjuntos e anula eles no novo resultado gerado.
'''

# v Comparação de conjuntos v

print(conjunto > {1,2}) # Contém
print({1,2} < conjunto) # Contido

conjunto.pop() # exclui o elemento

print(conjunto)