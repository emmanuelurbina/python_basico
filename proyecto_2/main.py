"""
Emmanuel Lucio Urbina 2020
Calculadora basica con functiones
Operaciones basicas (+ - * /)
"""
import os

menu = """
Menú Principal

1) Suma
2) Resta
3) Multiplicación
4) División
x) Salir

"""


def cls():
    """
    Limpia consola
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pasa_numero():
    """
    obtiene y valida un número entero o flotante
    """
    num = 0
    try:
        num = float(input("Ingresa número: "))
    except ValueError as err:
        print("Solo números__ Error: {}".format(err))
    finally:
        return num


def suma_fn(num_1=0, num_2=0):
    """
    suma de dos números
    """
    resultado = 0
    try:
        resultado = num_1 + num_2
    except ValueError as err:
        print("Ocurrio un error >_ {}".format(err))
    finally:
        return resultado


def resta_fn(num_1=0, num_2=0):
    """
    resta de dos números
    """
    resultado = 0
    try:
        resultado = num_1 - num_2
    except ValueError as err:
        print("Ocurrio un error >_ {}".format(err))
    finally:
        return resultado


def producto_fn(num_1=0, num_2=0):
    """
    producto de dos números
    """
    resultado = 0
    try:
        resultado = num_1 * num_2
    except ValueError as err:
        print("Ocurrio un error >_ {}".format(err))
    finally:
        return resultado


def division_fn(num_1=0, num_2=0):
    """
    division
    """
    resultado = 0
    try:
        resultado = num_1 / num_2
    except ZeroDivisionError as err:
        print("Ocurrio un error >_ {}".format(err))
    finally:
        return resultado


def calculadora():
    """
    Menú de calculadora.
    """
    continue_program = True

    while continue_program:
        print(menu)

        option = input("Escribe una opción del menú: ")
        if option == "1":
            cls()
            print("SUMA\n")
            num_1 = pasa_numero()
            num_2 = pasa_numero()
            resultado = suma_fn(num_1, num_2)
            print("El resultado es: {}".format(resultado))

        if option == "2":
            cls()
            print("Resta\n")
            num_1 = pasa_numero()
            num_2 = pasa_numero()
            resultado = resta_fn(num_1, num_2)
            print("El resultado es: {}".format(resultado))

        if option == "3":
            cls()
            print("MULTIPLICACIÓN\n")
            num_1 = pasa_numero()
            num_2 = pasa_numero()
            resultado = producto_fn(num_1, num_2)
            print("El resultado es: {}".format(resultado))

        if option == "4":
            cls()
            print("DIVISIÓN\n")
            num_1 = pasa_numero()
            num_2 = pasa_numero()
            resultado = division_fn(num_1, num_2)
            print("El resultado es: {}".format(resultado))

        if option == "x" or option == "X":
            continue_program = False
            print("Hasta luego...")

if __name__ == "__main__":
    calculadora()
