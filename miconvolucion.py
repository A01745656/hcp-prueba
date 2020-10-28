import numpy as np

def convolucion(A,B):
    C1 = 0
    for k in range(len(A)-1):
        for j in range (len(A)-1):
          N = A[k][j]*B[k][j]
          C1 += N
    C2 = 0    
    for k in range(len(A)-1):
        for j in range (len(A)-1):
          S = A[k][j+1]*B[k][j]
          C2 += S
    C3 = 0    
    for k in range(len(A)-1):
        for j in range (len(A)-1):
          T = A[k+1][j+1]*B[k][j]
          C3 += T
    C = [C1, C2, C3]
    
    return C


Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
def main():
  Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
  Filtro = [[1,0,2],[5,0,9],[6,2,1]]
  A=np.array(Matriz1)
  B=np.array(Filtro)
  C =np.zeros((2,2))
  C = convolucion(A,B)
  print (C)
    
main()
