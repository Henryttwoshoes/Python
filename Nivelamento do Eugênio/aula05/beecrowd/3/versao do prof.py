N = [0,0,0,0,0,0,0,0,0,0]
N[0] = int(input())
for i in range(1,10):
  N[i] = N[i-1]*2
for i in range(10):
  print(f'N[{i}] = {N[i]}')