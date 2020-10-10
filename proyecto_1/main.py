"""
Calculadora basica
Operaciones basicas (+ - * /)
"""
menu = """
Menú Principal

1) Suma
2) Resta
3) Multiplicación
4) División
x) Salir

"""
continue_program = True


if __name__ == "__main__":
    print(menu)
    op_1 = 0
    op_2 = 0
    res = 0
    while continue_program:

        option = input("Escribe una opción del menú: ")

        if option == "1":
            try:
                print("Suma")
                op_1 = float(input("Primer número: "))
                op_2 = float(input("Segundo número: "))
            except:
                print("Solo son validos enteros y decimales")
            finally:
                res = op_1 + op_2
                print("El resultado es: {}".format(res))

        if option == "2":
            try:
                print("Resta")
                op_1 = float(input("Primer número: "))
                op_2 = float(input("Segundo número: "))
            except:
                print("Solo son validos enteros y decimales")
            finally:
                res = op_1 - op_2
                print("El resultado es: {}".format(res))

        if option == "3":
            try:
                print("Multiplicación")
                op_1 = float(input("Primer número: "))
                op_2 = float(input("Segundo número: "))
            except:
                print("Solo son validos enteros y decimales")
            finally:
                res = op_1 * op_2
                print("El resultado es: {}".format(res))

        if option == "4":
            try:
                print("Resta")
                op_1 = float(input("Primer numero: "))
                op_2 = float(input("Segundo numero: "))
            except:
                print("Solo son validos enteros y decimales")
            finally:
                try:
                    res = round(op_1 / op_2, 4)
                except ZeroDivisionError as err:
                    print("No se puede dividir entre 0")
                finally:
                    print("El resultado es: {}".format(res))

        if option == "x" or option == "X":
            continue_program = False
            print("Hasta luego...")
