def triangular_superior(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i):
            if matriz[i][j] != 0:
                return False
    return True

def zero_diagonal(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i+1):
            if i == j:
                if matriz[i][j] == 0:
                    return False
    return True
                
def substituicao_regressiva(matriz, vetor):
    n = len(vetor)
    solucao = [0] * n
    
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz[i][j] * solucao[j]
        solucao[i] = (vetor[i] - soma) / matriz[i][i]
    
    return solucao

def ler_matriz(n):
    matriz = []
    print("Insira os elementos da matriz linha por linha:")
    for i in range(n):
        linha = input(f"Insira os elementos da linha {i+1} separados por espaço: ").strip().split()
        linha = [float(x) for x in linha]
        matriz.append(linha)
    return matriz

def ler_vetor(n):
    print("Insira os elementos do vetor separados por espaço:")
    vetor = input().strip().split()
    vetor = [float(x) for x in vetor]
    return vetor

def main():
    n = int(input("Digite a ordem da matriz: "))
    
    # Leitura da matriz
    matriz = ler_matriz(n)
    
    # Verificação se a matriz é triangular superior
    if not triangular_superior(matriz):
        print("A matriz não é triangular superior.")
        return
    
    # Verificação se a matriz tem 0 na diagonal principal
    if not zero_diagonal(matriz):
        print("A matriz possui 0 em sua diagonal principal.")
        return
    
    # Leitura do vetor
    vetor = ler_vetor(n)
    
    # Resolvendo o sistema
    solucao = substituicao_regressiva(matriz, vetor)
    
    # Exibindo a solução
    print("\nSolução:")
    for i, x in enumerate(solucao):
        print(f"x{i+1} =", x)

if __name__ == "__main__":
    main()