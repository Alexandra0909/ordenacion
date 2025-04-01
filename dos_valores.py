# Se trata de tomar una lista de dos valores desordenados
# Y producir una salida en orden creciente.

n = [15,23,35]
if n[0] > n[1] > n[2]:
    a = n[0]
    n[0] = n[1] = n[2]
    n[1] = a
    n[2] = a
print(n)
