import numpy as np

def main():
 
    # Definindo valores de n
    n_valores = [5, 15, 25]
 
    for n in n_valores:
        
        # Gerando vetores aleatórios
        u = np.random.rand(n, 1)
        v = np.random.rand(n, 1)

        #print(f"n = {n}:")
        #print(f"u = {u}")
        #print(f"v = {v}")
        
        # ||u||_2
        norma_u = np.linalg.norm(u, 2)
        print(f"||u||_2 = {norma_u}")
        
        # ||v||_2
        norma_v = np.linalg.norm(v, 2)
        print(f"||v||_2 = {norma_v}")
        
        A = np.outer(u, v.T)
                
        # ||A||_2
        norma_A = np.linalg.norm(A, 2)
        print(f"||A||_2 = {norma_A}")
        print(f'||u||*||v.T|| = {norma_u*norma_v}')
        
        # Posto de A
        posto_A = np.linalg.matrix_rank(A)
        print(f"Posto de A = {posto_A}")
        
        print("\n")
    
if __name__ == "__main__":
    main()
    
