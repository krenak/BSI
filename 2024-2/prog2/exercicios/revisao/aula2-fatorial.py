import math

def fatorial(n):
  if (n == 0) or (n == 1):
    return 1
  f = 1

  for i in range(1, n + 1):
    f = f * i
    return f

def fnSeno(angr):
  senoA = angr
  sinal = -1
  expoente = 3
  
  

def main():
  for anggraus in range(361):
    anggrad = math.radians(anggraus)
    seno = math.sin(anggraus)
    meuSeno = math.sin(anggrad)
    print(anggraus, math.sin(anggraus), math.cos(anggraus))

main()