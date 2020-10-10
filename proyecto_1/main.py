# Calculadora basica

menu = """
Menu Principal

1) Suma
2) Resta
3) Multiplicacion
4) Division
x) Salir

"""
opt = True


if __name__ == "__main__":
    print(menu)
    op_1 = 0
    op_2 = 0
    res = 0
    while opt:
        item = input("Escribe una opcion del menu: ")

        if item == "1":
            try:
                print("Suma")
                op_1 = float(input("Primer numero: "))
                op_2 = float(input("Segundo numero: "))
            except:
                print("Solo son validos enteros y decimales")
            finally:
                res = op_1 + op_2
                print("El resultado es: {}".format(res))

        if item == "x" or item == "X":
            opt = False
            print("Hasta luego...")
