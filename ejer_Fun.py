def suma(num_1:int (num_2)):
         return

menu_principal=True
while menu_principal:
    print("CALCUNEITOR 7000")
    print()
    print("1.sumar")
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.salir")
    try:
        op=int(input("\nEscribe tu opcion "))
        if op==1:
            print("\nSeleciono", op)
            a=int(input("Escribe un numero "))
            b=int(input("Escribe otro numero "))
            print("el resultado es tu mmama")

        if op==2:
            print("\nSeleciono", op)

        if op==3:
            print("\nSeleciono", op)

        if op==4:
            print("\nSeleciono", op)

        if op==5:
            print("\nSeleciono", op)
            menu_principal=False
            print("Gracias por calcular")

        if op<1 or op>5:
            print("\nopcion invalida")

    except ValueError:
        print("\nopcion invalida\n")