import numpy as np

tolerancia = 1e-5  # Define uma tolerância para lidar com erros de arredondamento

def is_orthogonal_by_definition(matrix):
    # Verifica se a matriz é quadrada
    n = len(matrix)
    if len(matrix) != len(matrix[0]):
        return False
    
    # Calcula a transposta da matriz
    transposta = np.transpose(matrix)

    # Calcula a matriz inversa
    if np.linalg.det(matrix) != 0:
        inversa = np.linalg.inv(matrix)
    else:
        return False
    
    # P^T = P^-1 ?
    if np.allclose(transposta, inversa, atol=tolerancia):
        return True
    else:
        return False
        
        
def is_orthogonal_by_vectors(matrix):
    # Verifica se a matriz é quadrada
    n = len(matrix)
    if len(matrix) != len(matrix[0]):
        return False
   
    # Verifica se as colunas têm tamanho unitário
    for j in range(n):
        norma_coluna = np.linalg.norm(matrix[j])
        if not np.isclose(norma_coluna, 1, atol=tolerancia):
            return False

    # Verifica se as colunas são ortogonais
    for i in range(n):
        for j in range(i + 1, n):
            produto_interno = np.dot(matrix[i], matrix[j])
            if not np.isclose(produto_interno, 0, atol=tolerancia):
                return False
    
    return True
    
    
def main():
    
    # Solicitando a matriz quadrada para o usuário
    n = int(input("Digite a ordem da matriz quadrada: "))
    print("Digite os elementos da matriz linha por linha:")
    matriz = []
    for _ in range(n):
        linha = list(map(float, input().split()))
        matriz.append(linha)

    # Verifica se a matriz é ortogonal e imprime o resultado
    if is_orthogonal_by_definition(matriz):
        print("A matriz é ortogonal por definição.")
    else:
        print("A matriz não é ortogonal por definição.")

    if is_orthogonal_by_vectors(matriz):
        print("A matriz é ortogonal pelo método dos vetores.")
    else:
        print("A matriz não é ortogonal pelo método dos vetores.")

if __name__ == "__main__":
    main()