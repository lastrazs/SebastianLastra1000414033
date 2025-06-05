def suma(a, b):
    "Función que suma dos números"
    return a + b

def resta(a, b):
    "Función que resta dos números"
    return a - b

def multiplicacion(a, b):
    "FUNCION QUE MULTIPLICA DOS NÚMEROS"
    return a * b

def division(a, b):
    "Función que divide dos números"
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print("¡Hola desde Python CI/CD!")
    print(f"2 + 3 = {suma(2, 3)}")
    print(f"5 - 1 = {resta(5, 1)}")
    print(f"4 * 6 = {multiplicacion(4, 6)}")
    print(f"8 / 2 = {division(8, 2)}")