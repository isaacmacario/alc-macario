import math

def lugar_geometrico(a, b):
    x = 15 * math.cos(a + b) + 20 * math.cos(a)
    y = 15 * math.sin(a + b) + 20 * math.sin(a)
    return x, y

def main():
    #Coletando a entrada
    a = float(input("Digite o valor de θ1: "))
    b = float(input("Digite o valor de θ2: "))
 
    #Convertendo graus para radianos
    a = a * math.pi / 180.0
    b = b * math.pi / 180.0
    
    # Posição do efetuador
    x, y = lugar_geometrico(a, b)
    
    #Formatando para 1 casa decimal
    x_arrendondado = round(x,1)
    y_arrendondado = round(y,1)
    
    # Exibindo a posição
    print(f"Coordenada X_U = {x_arrendondado}")
    print(f"Coordenada Y_U = {y_arrendondado}")

if __name__ == "__main__":
    main()