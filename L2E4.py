import numpy as np

def norma_2(n, vetor):
    
    # Calculando o módulo dos elementos
    vetor_modulo = np.abs(vetor)
    
    # Elevando ao quadrado
    vetor_quadrado = vetor_modulo ** 2
    
    # Somatório dos elementos
    somatorio = np.sum(vetor_quadrado)
    
    # Raíz quadrada do somatório
    norma2 = np.sqrt(somatorio)
    
    return norma2

def main():
 
    # Definindo valores de n
    n_valores = [5, 15, 25]
 
    for n in n_valores:
        
        # Gerando vetores aleatórios
        u = np.random.rand(n, 1)
        v = np.random.rand(n, 1)

        print(f"n = {n}:")
        print(f"u = {u}")
        print(f"v = {v}")
        
        # ||u||_2
        norma_u = norma_2(n,u)
        print(f"||u||_2 = {norma_u}")
        
        # ||v||_2
        norma_v = norma_2(n,v)
        print(f"||v||_2 = {norma_v}")
        
        A = np.outer(u, v.T)
        print(f"A = {A}")
        
        # ||A||_2
        norma_A = norma_2(n,A)
        print(f"||A||_2 = {norma_A}")
        
        # Posto de A
        posto_A = np.linalg.matrix_rank(A)
        print(f"Posto de A = {posto_A}")
        
        print("\n")
    
if __name__ == "__main__":
    main()