# Módulo dibujos

def cuadrado(x,N):
    """
    x - cadena
    N - número entero positivo
    dibuja un cuadrado con el N símbolos x
    """
    for u in range(N):
        print(N*x)
        
        
def cuadrado_vacio(x,N):
    """
    x - cadena
    N - número entero positivo
    dibuja el perímetro de un cuadrado con el N símbolos x
    """
    if N == 1:
        print(x)
    else:
        print(N*x)
        A = x
        for u in range(N - 2):
            print(x + (N - 2)*' ' + 'a')
        print(N*x)
    