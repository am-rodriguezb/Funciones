from ejemp_func2 import *

menu_principal=True
while menu_principal:
    print("CALCUNEITOR 8500")
    print()
    print("1.Calcular IVA")
    print("2.DEscuento de producto")
    print("3.multiplicar")
    print("4.salir")
    try:
        op=int(input("\nEscribe tu opcion "))
        if op==1:
            print("\nSeleciono", op)
            calcular_iva(100000)
        if op==2:
            print("\nSeleciono", op)
            print(descuento_producto(20000,40))
        if op==3:
            print("\nSeleciono", op)
            print(calcular_IMC(75,1.69))
        if op==4:
            print("\nSeleciono", op)
            menu_principal=False
            print("Gracias por calcular")

        if op<1 or op>4:
            print("\nopcion invalida")

    except ValueError:
        print("\nopcion invalida\n")