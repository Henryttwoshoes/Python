# continue força a próxima interação
# Também se aplica para outros comandos como while

for n in range(10):
  if n % 2 == 0:
    continue
  print(n)